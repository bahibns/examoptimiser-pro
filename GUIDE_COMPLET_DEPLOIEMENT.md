# 🎯 GUIDE COMPLET DE DÉPLOIEMENT - ÉTAPE PAR ÉTAPE

## ⏱️ TEMPS ESTIMÉ : 30 minutes

---

# PARTIE 1 : CRÉER UN COMPTE GITHUB (5 minutes)

## Étape 1.1 : Aller sur GitHub
1. Ouvrez votre navigateur web (Chrome, Firefox, Edge...)
2. Tapez dans la barre d'adresse : **https://github.com**
3. Appuyez sur **Entrée**

## Étape 1.2 : Créer un compte
1. Cliquez sur le bouton **"Sign up"** (en haut à droite)
2. Remplissez le formulaire :
   - **Email** : Entrez votre adresse email (ex: votreemail@gmail.com)
   - **Password** : Créez un mot de passe fort (ex: MonMotDePasse123!)
   - **Username** : Choisissez un nom d'utilisateur (ex: bahi-exams)
   - **Email preferences** : Décochez la case si vous ne voulez pas recevoir d'emails
3. Cliquez sur **"Continue"**
4. Résolvez le puzzle de vérification
5. GitHub vous enverra un code à votre email
6. Ouvrez votre email
7. Copiez le code reçu (6 chiffres)
8. Revenez sur GitHub
9. Collez le code dans la case
10. Cliquez sur **"Continue"**

## Étape 1.3 : Finaliser le profil
1. GitHub vous posera quelques questions
2. Répondez rapidement ou cliquez **"Skip personalization"** en bas
3. Vous êtes maintenant sur votre tableau de bord GitHub !

---

# PARTIE 2 : CRÉER UN REPOSITORY (DÉPÔT) SUR GITHUB (5 minutes)

## Étape 2.1 : Créer un nouveau repository
1. Sur la page GitHub, cliquez sur le **bouton vert "New"** (ou le **+** en haut à droite → "New repository")
2. Remplissez le formulaire :

   **Repository name*** (OBLIGATOIRE)
   ```
   exam-scheduler
   ```
   
   **Description** (optionnel)
   ```
   Plateforme d'optimisation des emplois du temps d'examens universitaires
   ```
   
   **Public/Private**
   - ✅ Cochez **"Public"** (c'est gratuit et nécessaire pour Streamlit Cloud gratuit)
   
   **Initialize this repository with:**
   - ❌ NE COCHEZ RIEN (pas de README, pas de .gitignore, pas de licence)

3. Cliquez sur le bouton vert **"Create repository"** en bas

## Étape 2.2 : Vous êtes sur la page de votre nouveau repository
Vous devriez voir une page avec des instructions. **GARDEZ CETTE PAGE OUVERTE**, nous allons l'utiliser plus tard.

---

# PARTIE 3 : UPLOADER VOTRE CODE SUR GITHUB (10 minutes)

## 🖥️ IMPORTANT : Vous devez installer Git sur votre ordinateur

### Sur Windows :

#### Étape 3.1 : Télécharger Git
1. Allez sur : **https://git-scm.com/download/win**
2. Le téléchargement commence automatiquement
3. Ouvrez le fichier téléchargé (ex: Git-2.43.0-64-bit.exe)
4. Installation :
   - Cliquez sur **"Next"** pour toutes les étapes
   - Laissez les options par défaut
   - Cliquez sur **"Install"**
   - Cliquez sur **"Finish"**

#### Étape 3.2 : Ouvrir Git Bash
1. Appuyez sur la touche **Windows** de votre clavier
2. Tapez : **git bash**
3. Cliquez sur **"Git Bash"**
4. Une fenêtre noire s'ouvre (c'est normal !)

#### Étape 3.3 : Configurer Git (PREMIÈRE FOIS SEULEMENT)
Dans Git Bash, tapez ces commandes **UNE PAR UNE** (appuyez sur Entrée après chaque ligne) :

```bash
git config --global user.name "VOTRE_NOM"
```
Remplacez VOTRE_NOM par votre nom (ex: Bahi)

Appuyez sur **Entrée**

```bash
git config --global user.email "VOTRE_EMAIL@example.com"
```
Remplacez par l'email que vous avez utilisé pour GitHub

Appuyez sur **Entrée**

#### Étape 3.4 : Aller dans le dossier de votre projet
Dans Git Bash, tapez :

```bash
cd /c/Users/BAHI/Downloads
```

**⚠️ ADAPTEZ CE CHEMIN** selon où vous avez extrait votre projet !

Pour trouver le bon chemin :
1. Ouvrez l'Explorateur Windows
2. Naviguez jusqu'au dossier de votre projet
3. Cliquez dans la barre d'adresse en haut
4. Copiez le chemin (ex: C:\Users\BAHI\Documents\MonProjet)
5. Remplacez les \ par des /
6. Remplacez C: par /c/
7. Exemple : C:\Users\BAHI\Documents\MonProjet devient /c/Users/BAHI/Documents/MonProjet

#### Étape 3.5 : Initialiser Git dans votre projet
Tapez cette commande :

```bash
git init
```

Vous devriez voir : "Initialized empty Git repository..."

#### Étape 3.6 : Ajouter tous les fichiers
Tapez :

```bash
git add .
```

(N'oubliez pas le point !)

#### Étape 3.7 : Créer votre premier commit
Tapez :

```bash
git commit -m "Initial commit - Exam Scheduler"
```

#### Étape 3.8 : Renommer la branche en "main"
Tapez :

```bash
git branch -M main
```

#### Étape 3.9 : Connecter à GitHub

**RETOURNEZ sur la page GitHub de votre repository que vous avez gardée ouverte.**

Vous devriez voir une section "…or push an existing repository from the command line"

Copiez la première ligne qui ressemble à :
```
git remote add origin https://github.com/VOTRE_USERNAME/exam-scheduler.git
```

**Collez-la dans Git Bash** et appuyez sur Entrée

#### Étape 3.10 : Envoyer votre code sur GitHub
Tapez :

```bash
git push -u origin main
```

**GitHub va vous demander de vous connecter :**
1. Une fenêtre s'ouvre
2. Cliquez sur **"Sign in with your browser"**
3. Connectez-vous avec votre compte GitHub
4. Cliquez sur **"Authorize"**
5. Revenez à Git Bash

Le code s'upload ! (Cela peut prendre 1-2 minutes)

#### Étape 3.11 : Vérifier
1. Retournez sur la page GitHub de votre repository
2. Appuyez sur **F5** pour rafraîchir
3. Vous devriez voir tous vos fichiers !

✅ **BRAVO ! Votre code est sur GitHub !**

---

# PARTIE 4 : CRÉER UNE BASE DE DONNÉES POSTGRESQL (7 minutes)

## Étape 4.1 : Créer un compte Supabase
1. Allez sur : **https://supabase.com**
2. Cliquez sur **"Start your project"**
3. Cliquez sur **"Sign in with GitHub"**
4. Connectez-vous avec votre compte GitHub
5. Cliquez sur **"Authorize supabase"**

## Étape 4.2 : Créer un nouveau projet
1. Cliquez sur **"New project"**
2. Remplissez le formulaire :

   **Name**
   ```
   exam-scheduler-db
   ```
   
   **Database Password** (TRÈS IMPORTANT !)
   Créez un mot de passe FORT et **NOTEZ-LE QUELQUE PART** (vous en aurez besoin plus tard !)
   Exemple : `MonMotDePasse2024!ExamDB`
   
   **Region**
   Choisissez le plus proche de vous (ex: "Europe West (London)")
   
   **Pricing Plan**
   - Laissez **"Free"** sélectionné

3. Cliquez sur **"Create new project"**

⏱️ **ATTENDEZ 2 MINUTES** - Supabase crée votre base de données

## Étape 4.3 : Récupérer les informations de connexion
1. Quand le projet est créé, cliquez sur **"Settings"** (icône engrenage en bas à gauche)
2. Cliquez sur **"Database"**
3. Descendez jusqu'à "Connection string"
4. Cliquez sur **"URI"**
5. Vous verrez quelque chose comme :
   ```
   postgresql://postgres.[xxxxx]:[YOUR-PASSWORD]@aws-0-eu-west-1.pooler.supabase.com:6543/postgres
   ```

**NOTEZ CES INFORMATIONS** (nous en aurons besoin) :
- **Host** : aws-0-eu-west-1.pooler.supabase.com (ou similaire)
- **Port** : 6543 (ou 5432)
- **Database** : postgres
- **User** : postgres
- **Password** : Celui que vous avez créé à l'étape 4.2

## Étape 4.4 : Initialiser la base de données
1. Cliquez sur **"SQL Editor"** dans le menu de gauche
2. Cliquez sur **"New query"**
3. **OUVREZ** le fichier `database/schema.sql` de votre projet sur votre ordinateur
4. **COPIEZ** tout son contenu (Ctrl+A puis Ctrl+C)
5. **COLLEZ** dans l'éditeur SQL de Supabase
6. Cliquez sur **"RUN"** (en bas à droite)
7. Vous devriez voir "Success. No rows returned"

8. Cliquez à nouveau sur **"New query"**
9. **OUVREZ** le fichier `database/indexes.sql`
10. **COPIEZ** tout son contenu
11. **COLLEZ** dans l'éditeur SQL
12. Cliquez sur **"RUN"**

✅ **Votre base de données est prête !**

---

# PARTIE 5 : DÉPLOYER SUR STREAMLIT CLOUD (5 minutes)

## Étape 5.1 : Créer un compte Streamlit Cloud
1. Allez sur : **https://streamlit.io/cloud**
2. Cliquez sur **"Sign up"**
3. Cliquez sur **"Continue with GitHub"**
4. Connectez-vous avec votre compte GitHub
5. Cliquez sur **"Authorize streamlit"**

## Étape 5.2 : Créer une nouvelle app
1. Cliquez sur **"New app"** (bouton bleu en haut à droite)
2. Remplissez le formulaire :

   **Repository**
   Sélectionnez : `VOTRE_USERNAME/exam-scheduler`
   
   **Branch**
   Laissez : `main`
   
   **Main file path**
   Tapez : `app.py`

3. Cliquez sur **"Advanced settings"**

## Étape 5.3 : Ajouter les secrets (TRÈS IMPORTANT !)
Dans la section **"Secrets"**, collez ce texte :

**⚠️ REMPLACEZ LES VALEURS PAR LES VRAIES INFORMATIONS DE SUPABASE** (de l'étape 4.3) :

```toml
DB_HOST = "aws-0-eu-west-1.pooler.supabase.com"
DB_PORT = "6543"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "MonMotDePasse2024!ExamDB"
```

**Exemple avec de vraies valeurs :**
Si votre connection string Supabase était :
`postgresql://postgres.abcdefgh:MyPass123!@aws-0-us-east-1.pooler.supabase.com:5432/postgres`

Alors vous écrivez :
```toml
DB_HOST = "aws-0-us-east-1.pooler.supabase.com"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "MyPass123!"
```

## Étape 5.4 : Déployer !
1. Vérifiez que tout est correct
2. Cliquez sur **"Deploy"** (bouton bleu en bas)

⏱️ **ATTENDEZ 2-3 MINUTES** - Streamlit déploie votre application

## Étape 5.5 : Tester votre application
1. Quand le déploiement est terminé, vous verrez votre application !
2. Elle sera accessible à l'adresse : `https://VOTRE_USERNAME-exam-scheduler-xxxxxx.streamlit.app`

---

# 🎉 FÉLICITATIONS !

Votre application est maintenant **EN LIGNE** et accessible par **TOUT LE MONDE** sur Internet !

## 🔗 Votre lien
Vous pouvez partager le lien de votre application à vos collègues, étudiants, professeurs !

## ⚙️ Gérer votre application

### Pour modifier votre code :
1. Modifiez vos fichiers localement
2. Dans Git Bash :
   ```bash
   git add .
   git commit -m "Description de vos modifications"
   git push
   ```
3. Streamlit Cloud détectera automatiquement les changements et redéploiera !

### Pour voir les logs (erreurs) :
1. Allez sur https://streamlit.io/cloud
2. Cliquez sur votre app
3. Cliquez sur "Manage app"
4. Cliquez sur "Logs"

### Pour redémarrer l'application :
1. Allez sur https://streamlit.io/cloud
2. Cliquez sur les 3 points ⋮ à côté de votre app
3. Cliquez sur "Reboot"

---

# ⚠️ PROBLÈMES COURANTS

## Problème 1 : "Failed to connect to database"
**Solution** : Vérifiez vos secrets dans Streamlit Cloud
1. Allez sur https://streamlit.io/cloud
2. Cliquez sur votre app → "Settings"
3. Vérifiez que DB_HOST, DB_PASSWORD, etc. sont corrects

## Problème 2 : "ModuleNotFoundError"
**Solution** : Vérifiez que `requirements.txt` contient tous les modules
1. Ajoutez le module manquant dans `requirements.txt`
2. Commitez et push sur GitHub

## Problème 3 : L'app ne démarre pas
**Solution** : Regardez les logs
1. Streamlit Cloud → Votre app → "Manage app" → "Logs"
2. Lisez l'erreur et cherchez sur Google

## Problème 4 : "git push" demande username/password
**Solution** : Utilisez un token d'accès personnel
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → Cochez "repo"
3. Copiez le token
4. Utilisez le token comme mot de passe lors du push

---

# 📞 BESOIN D'AIDE ?

- Documentation Streamlit : https://docs.streamlit.io
- Documentation Supabase : https://supabase.com/docs
- Documentation Git : https://git-scm.com/doc

---

# ✅ CHECKLIST FINALE

- [ ] Compte GitHub créé
- [ ] Repository créé sur GitHub
- [ ] Git installé sur votre ordinateur
- [ ] Code uploadé sur GitHub
- [ ] Compte Supabase créé
- [ ] Base de données PostgreSQL créée
- [ ] Schéma SQL exécuté dans Supabase
- [ ] Compte Streamlit Cloud créé
- [ ] Application déployée
- [ ] Secrets configurés
- [ ] Application accessible en ligne

---

# 🎯 PROCHAINES ÉTAPES

Maintenant que votre application est en ligne, vous pouvez :
1. Générer des données de test via l'interface d'administration
2. Inviter des utilisateurs à tester
3. Personnaliser l'interface
4. Ajouter de nouvelles fonctionnalités

**BONNE CHANCE !** 🚀
