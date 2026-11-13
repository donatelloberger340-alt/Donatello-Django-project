# TechActu - projet Django

## Parcours du site
- `/` : page d'accueil
- `/articles/` : liste des articles (portable, ordinateur, etc.)
- `/articles/1/` : détail d'un article

## Lancer le projet
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Pour ajouter des articles :
```bash
python manage.py createsuperuser
```
Puis aller sur `/admin/` et créer les articles.
