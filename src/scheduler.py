from datetime import datetime, timedelta
from typing import List, Dict, Tuple
import random

class ExamScheduler:
    """Ultra-fast scheduling algorithm optimized for <10 second execution"""
    
    def __init__(self, db):
        self.db = db
    
    def generate_schedule(self, periode_id: int, annee_universitaire: str) -> Tuple[bool, Dict]:
        start_time = datetime.now()
        
        periode = self.db.execute_query(
            "SELECT * FROM periodes_examen WHERE id = %s", 
            (periode_id,)
        )[0]
        
        date_debut = periode['date_debut']
        date_fin = periode['date_fin']
        
        # Load all data 
        modules = self.db.get_modules_with_inscriptions()
        modules = sorted(modules, key=lambda x: x['nb_inscrits'], reverse=True)
        
        salles = self.db.get_lieu_examen()
        # Sort by capacity ASCENDING (Best Fit strategy)
        salles_by_capacity = sorted(salles, key=lambda x: x['capacite_examen'])
        
        professeurs = self.db.get_professeurs()
        prof_by_dept = {}
        for p in professeurs:
            if p['dept_id'] not in prof_by_dept:
                prof_by_dept[p['dept_id']] = []
            prof_by_dept[p['dept_id']].append(p)
        
        self.db.delete_all_examens(periode_id)
        
        time_slots = [(8, 30), (11, 0), (14, 30)]  
        
        effective_days = (date_fin - date_debut).days + 1
        available_dates = [(date_debut + timedelta(days=i)) for i in range(effective_days)]
        
        room_schedule = {} 
        prof_schedule = {}
        prof_daily_count = {}
        prof_global_count = {p['id']: 0 for p in professeurs}
        
        student_exams = {}
        student_dates = {}
        
        print("Loading enrollments...")
        enrollments = self.db.execute_query(
            "SELECT module_id, etudiant_id FROM inscriptions WHERE statut = 'inscrit'"
        )
        module_students = {}
        student_modules = {}
        for enroll in enrollments:
            mid = enroll['module_id']
            sid = enroll['etudiant_id']
            
            if mid not in module_students:
                module_students[mid] = set()
            module_students[mid].add(sid)
            
            if sid not in student_modules:
                student_modules[sid] = set()
            student_modules[sid].add(mid)
        
        student_daily_exams = {}  
        
        exams_to_insert = []
        surveillances_to_insert = []
        
        scheduled_count = 0
        failed_modules = []
        
        current_slot_index = 0
        total_slots = len(available_dates) * len(time_slots)
        
        for module in modules:
            module_id = module['id']
            nb_inscrits = module['nb_inscrits']
            students = module_students.get(module_id, set())
            
            scheduled = False
            
            
            suitable_rooms = [s for s in salles_by_capacity if s['capacite_examen'] >= nb_inscrits]
            
            if not suitable_rooms:
                failed_modules.append({'module': module['nom'], 'nb_inscrits': nb_inscrits})
                continue
            
            
            attempts = 0
            max_attempts = min(200, total_slots * 3) 
            
            while not scheduled and attempts < max_attempts:
                slot_idx = (current_slot_index + attempts) % total_slots
                date_idx = slot_idx // len(time_slots)
                time_idx = slot_idx % len(time_slots)
                
                if date_idx >= len(available_dates):
                    break
                
                exam_date = available_dates[date_idx]
                slot_hour, slot_minute = time_slots[time_idx]
                exam_datetime = datetime.combine(
                    exam_date,
                    datetime.min.time().replace(hour=slot_hour, minute=slot_minute)
                )
                
                suitable_room = None
                exam_end_datetime = exam_datetime + timedelta(minutes=module['duree_examen'])
                
                for room in suitable_rooms:
                    room_id = room['id']
                    
                    room_available = True
                    if room_id in room_schedule:
                        for existing_start, existing_end in room_schedule[room_id]:
                            
                            if not (exam_end_datetime <= existing_start or exam_datetime >= existing_end):
                                room_available = False
                                break
                    
                    if room_available:
                        suitable_room = room
                        break
                
                if not suitable_room:
                    attempts += 1
                    continue
                
                rest_day_conflict = False
                for student_id in students:
                    prev_day = exam_date - timedelta(days=1)
                    next_day = exam_date + timedelta(days=1)
                    
                    s_dates = student_dates.get(student_id, set())
                    if prev_day in s_dates or next_day in s_dates:
                        rest_day_conflict = True
                        break
                
                if rest_day_conflict:
                    attempts += 1
                    continue
                
                dept_profs = prof_by_dept.get(module['dept_id'], professeurs[:10])
                


                required_profs = 3 
                assigned_profs = [] 

                def get_sorted_candidates(candidates):
                    return sorted(candidates, key=lambda p: (prof_global_count.get(p['id'], 0), p['id']))

                # --- Step 1: Select Responsible 
                responsible = None
                
                # Filter dept profs available now
                candidates_dept = [
                    p for p in dept_profs 
                    if prof_daily_count.get((p['id'], exam_date), 0) < 3 
                    and (p['id'], exam_datetime) not in prof_schedule
                ]
                candidates_dept = get_sorted_candidates(candidates_dept)
                
                if candidates_dept:
                    responsible = candidates_dept[0]
                else:
                    # Fallback: Responsible from ANY department
                    candidates_all = [
                        p for p in professeurs
                        if prof_daily_count.get((p['id'], exam_date), 0) < 3
                        and (p['id'], exam_datetime) not in prof_schedule
                    ]
                    candidates_all = get_sorted_candidates(candidates_all)
                    if candidates_all:
                         responsible = candidates_all[0]
                
                if not responsible:
                    attempts += 1 
                    continue
                    
                assigned_profs.append((responsible, 'responsable'))
                
                # --- Step 2: Select 2 Surveillants 
                nb_surveillants_needed = 2
                surveillants_found = []
                
                # Try Dept candidates first
                potentials_dept = [
                    p for p in dept_profs 
                    if p['id'] != responsible['id']
                    and prof_daily_count.get((p['id'], exam_date), 0) < 3 
                    and (p['id'], exam_datetime) not in prof_schedule
                ]
                potentials_dept = get_sorted_candidates(potentials_dept)
                
                surveillants_found.extend(potentials_dept[:nb_surveillants_needed])
                
                # If still need more, check ALL profs
                if len(surveillants_found) < nb_surveillants_needed:
                    needed = nb_surveillants_needed - len(surveillants_found)
                    current_ids = {p['id'] for p in surveillants_found} | {responsible['id']}
                    
                    potentials_all = [
                        p for p in professeurs
                        if p['id'] not in current_ids
                        and prof_daily_count.get((p['id'], exam_date), 0) < 3
                        and (p['id'], exam_datetime) not in prof_schedule
                    ]
                    potentials_all = get_sorted_candidates(potentials_all)
                    surveillants_found.extend(potentials_all[:needed])

                for s in surveillants_found:
                    assigned_profs.append((s, 'surveillant'))

                student_conflict = False
                for student_id in students:
                    student_key = (student_id, exam_date)
                    if student_daily_exams.get(student_key, 0) >= 1:
                        student_conflict = True
                        break
                
                if student_conflict:
                    attempts += 1
                    continue
                
                # All checks passed - schedule exam
                # Update tracking for ALL assigned profs
                for prof, role in assigned_profs:
                     prof_time_key = (prof['id'], exam_datetime)
                     prof_schedule[prof_time_key] = True
                     
                     prof_key = (prof['id'], exam_date)
                     prof_daily_count[prof_key] = prof_daily_count.get(prof_key, 0) + 1
                     
                     prof_global_count[prof['id']] += 1


                exams_to_insert.append({
                    'module_id': module_id,
                    'prof_id': responsible['id'], 
                    'salle_id': suitable_room['id'],
                    'periode_id': periode_id,
                    'date_heure': exam_datetime,
                    'duree_minutes': module['duree_examen'],
                    'nb_inscrits': nb_inscrits,
                    'surveillants': [p['id'] for p, role in assigned_profs if role == 'surveillant']
                })
                
                # Update room tracking
                room_id = suitable_room['id']
                if room_id not in room_schedule:
                    room_schedule[room_id] = []
                room_schedule[room_id].append((exam_datetime, exam_end_datetime))
                
                for student_id in students:
                    student_key = (student_id, exam_date)
                    student_daily_exams[student_key] = student_daily_exams.get(student_key, 0) + 1
                    
                    if student_id not in student_dates:
                        student_dates[student_id] = set()
                    student_dates[student_id].add(exam_date)
                
                scheduled = True
                scheduled_count += 1
                current_slot_index = (slot_idx + 1) % total_slots
                
                attempts += 1
            
            if not scheduled:
                failed_modules.append({'module': module['nom'], 'nb_inscrits': nb_inscrits})
        
        # Batch insert all exams first
        print(f"Inserting {len(exams_to_insert)} exams...")
        
        # Prepare data for batch insert
        batch_exams = []
        batch_surveillances = []
        
        for exam_data in exams_to_insert:
            batch_exams.append((
                exam_data['module_id'],
                exam_data['prof_id'], # Responsible
                exam_data['salle_id'],
                exam_data['periode_id'],
                exam_data['date_heure'],
                exam_data['duree_minutes'],
                exam_data['nb_inscrits']
            ))
            
            # Add Responsible surveillance
            batch_surveillances.append((
                exam_data['module_id'], 
                exam_data['periode_id'], 
                exam_data['prof_id'], 
                'responsable'
            ))
            
            # Add Assistant surveillances
            for surv_id in exam_data.get('surveillants', []):
                batch_surveillances.append((
                    exam_data['module_id'], 
                    exam_data['periode_id'], 
                    surv_id, 
                    'surveillant'
                ))
        
        if batch_exams:
            self.db.batch_insert_exams(batch_exams, batch_surveillances)
        
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()
        
        # Get conflicts
        conflicts, total_conflicts = self.get_conflicts()
        
        result = {
            'scheduled': scheduled_count,
            'failed': len(failed_modules),
            'failed_modules': failed_modules[:10],
            'execution_time': execution_time,
            'conflicts': conflicts,
            'total_conflicts': total_conflicts
        }
        
        return True, result
    
    def optimize_schedule(self, periode_id: int):
        from src.constraints import ConstraintChecker
        constraint_checker = ConstraintChecker(self.db)
        
        query = """
            SELECT ex.id, ex.salle_id, ex.nb_inscrits, l.capacite_examen,
                   l.capacite_examen - ex.nb_inscrits as espace_libre
            FROM examens ex
            JOIN lieu_examen l ON ex.salle_id = l.id
            WHERE ex.periode_id = %s
              AND l.capacite_examen - ex.nb_inscrits > 4
            ORDER BY espace_libre DESC
        """
        
        underutilized = self.db.execute_query(query, (periode_id,))
        
        optimizations = 0
        for exam in underutilized:
            smaller_rooms = self.db.execute_query("""
                SELECT id, nom, capacite_examen
                FROM lieu_examen
                WHERE capacite_examen >= %s
                  AND capacite_examen < %s
                ORDER BY capacite_examen ASC
                LIMIT 1
            """, (exam['nb_inscrits'], exam['capacite_examen']))
            
            if smaller_rooms:
                new_room = smaller_rooms[0]
                exam_data = self.db.execute_query(
                    "SELECT date_heure, duree_minutes FROM examens WHERE id = %s",
                    (exam['id'],)
                )[0]
                
                valid, _ = constraint_checker.check_room_availability(
                    new_room['id'],
                    exam_data['date_heure'],
                    exam_data['duree_minutes']
                )
                
                if valid:
                    self.db.execute_query(
                        "UPDATE examens SET salle_id = %s WHERE id = %s",
                        (new_room['id'], exam['id']),
                        fetch=False
                    )
                    optimizations += 1
        
        return optimizations
    
    def get_conflicts(self):
        """Fast conflict detection"""
        try:
            conflicts = {
                'etudiants': self.db.execute_query("SELECT * FROM conflits_etudiants LIMIT 100") or [],
                'professeurs': self.db.execute_query("SELECT * FROM conflits_professeurs LIMIT 100") or [],
                'capacite': self.db.execute_query("SELECT * FROM conflits_capacite LIMIT 100") or [],
                'salles': self.db.execute_query("SELECT * FROM conflits_salles LIMIT 100") or []
            }
            total = sum(len(v) for v in conflicts.values())
            return conflicts, total
        except:
            return {'etudiants': [], 'professeurs': [], 'capacite': [], 'salles': []}, 0
