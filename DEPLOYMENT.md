# 🎓 ExamOptimizer Pro - Guide de Déploiement

## 📋 Prérequis
- Compte GitHub
- Compte Streamlit Cloud
- Base de données PostgreSQL (Supabase ou Neon)

## 🚀 Déploiement sur Streamlit Cloud

### 1. Base de données PostgreSQL (Supabase - GRATUIT)
1. Allez sur https://supabase.com
2. Créez un compte
3. Cliquez sur "New Project"
4. Remplissez :
   - **Name** : exam-scheduler-db
   - **Database Password** : Créez un mot de passe fort (NOTEZ-LE !)
   - **Region** : Choisissez le plus proche de vous
5. Attendez 2 minutes que la DB soit créée
6. Cliquez sur "Settings" → "Database"
7. Notez les informations de connexion :
   - Host
   - Database name
   - Port (5432)
   - User (postgres)
   - Password (celui que vous avez créé)

### 2. Initialiser la base de données
1. Retournez sur Supabase
2. Cliquez sur "SQL Editor" (dans le menu gauche)
3. Ouvrez le fichier `database/schema.sql` de ce projet
4. Copiez tout le contenu
5. Collez dans l'éditeur SQL de Supabase
6. Cliquez sur "RUN"
7. Répétez pour `database/indexes.sql`

### 3. Déployer sur Streamlit Cloud
1. Allez sur https://streamlit.io/cloud
2. Cliquez sur "Sign up" → Connectez-vous avec GitHub
3. Autorisez Streamlit à accéder à vos repositories
4. Cliquez sur "New app"
5. Remplissez :
   - **Repository** : Sélectionnez votre repository GitHub
   - **Branch** : main
   - **Main file path** : app.py
6. Cliquez sur "Advanced settings"
7. Dans "Secrets", copiez-collez ceci (REMPLACEZ avec vos vraies valeurs de Supabase) :

```toml
DB_HOST = "db.xxxxxxxxxxxxx.supabase.co"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "votre_mot_de_passe_supabase"
```

8. Cliquez sur "Deploy"
9. Attendez 2-3 minutes

### 4. Générer les données de test
Une fois l'app déployée :
1. Ouvrez votre app Streamlit
2. Allez dans la page "Administration"
3. Utilisez les fonctions d'importation pour ajouter des données

## ✅ C'est fait !
Votre application est maintenant en ligne et accessible à tous !

## 🔗 Liens Utiles
- Streamlit Cloud : https://streamlit.io/cloud
- Supabase : https://supabase.com
- Documentation : https://docs.streamlit.io

## ⚠️ Important
- Ne commitez JAMAIS le fichier `.env` sur GitHub (il est déjà dans .gitignore)
- Utilisez toujours les "Secrets" de Streamlit Cloud pour les informations sensibles
- La version gratuite de Supabase a des limites : 500 MB de stockage, 2 GB de bande passante
