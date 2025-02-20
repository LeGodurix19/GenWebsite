# Générateur Automatique de Site Web avec Django

## 📌 Introduction
Ce programme automatise la création d'un site web Django en générant un projet structuré basé sur des composants modulaires. Il permet de créer facilement un site dynamique en demandant des informations sur les pages et leurs composants.

## 🚀 Fonctionnalités
- **Création automatique d'un projet Django**
- **Génération dynamique des fichiers `views.py`, `urls.py` et templates HTML**
- **Utilisation de composants réutilisables** (HTML, JS et Python)
- **Système de menu généré dynamiquement**
- **Copie sélective des fichiers des composants**
- **Utilisation de Tailwind CSS pour un design moderne**

## 📂 Structure du Projet
```
📁 generated_site/
 ├── 📁 main/                 # Application Django
 │   ├── 📁 templates/        # Dossier des templates HTML
 │   │   ├── 📁 components/   # Dossier des composants HTML
 │   │   ├── base.html        # Template principal
 │   │   ├── index.html       # Page d'accueil générée dynamiquement
 │   ├── views.py            # Gestion des vues Django
 │   ├── urls.py             # Routes du site
 ├── 📁 components/          # Dossier des composants personnalisables
 ├── manage.py               # Script principal Django
```

## ⚙️ Comment ça fonctionne ?
1. **Saisie de l'utilisateur**
   - L'utilisateur définit le nombre de pages et sélectionne les composants.
   - Le programme récupère automatiquement tous les composants disponibles.

2. **Génération du projet Django**
   - Un projet Django est créé avec une application `main`.
   - Le fichier `settings.py` est mis à jour pour inclure `main`.

3. **Création et copie des composants**
   - Seuls les fichiers pertinents (`.html`, `.js`, `.css`) des composants sont copiés.
   - Un fichier `menu.html` est généré dynamiquement pour la navigation.

4. **Création des templates et routes**
   - Les templates sont générés pour chaque page avec les composants inclus.
   - `views.py` et `urls.py` sont mis à jour automatiquement.

5. **Lancement du serveur Django**
   - Le projet est prêt à être testé avec `python3 manage.py runserver`.

## 📜 Installation et Exécution
### 1️⃣ Prérequis
Assurez-vous d'avoir **Python 3** et **Django** installés :
```bash
pip install django
```

### 2️⃣ Exécuter le programme
```bash
python3 generate.py
```
Suivez les instructions pour définir vos pages et composants.

### 3️⃣ Lancer le serveur Django
```bash
cd generated_site
python3 manage.py runserver
```

## 📦 Ajouter un Composant
Pour ajouter un nouveau composant au projet, suivez ces règles :
1. **Créer un dossier dans `components/`** avec le nom du composant (ex: `carousel`).
2. **Ajouter les fichiers nécessaires** dans ce dossier :
   - `carousel.html` : Code HTML du composant.
   <!-- - `carousel.css` : Styles spécifiques au composant (optionnel). -->
   - `carousel.js` : Fonctionnalités interactives (optionnel).
   - `carousel.py` : Code Python si le composant doit manipuler des données (optionnel).
3. **Respecter la structure de code suivante** :
   - Le fichier `.html` doit inclure uniquement **le bloc de code du composant** et non un document HTML complet.
   - Le fichier `.js` doit gérer **uniquement l'interactivité du composant**.
   - Le fichier `.py` doit contenir **le code Python** nécessaires a implementer dans la fonction vue CA NE DOIT PAS ETRE UNE FONCTION.
   Merci d'aller voir les components deja existant pour voir comment cela est fait
   Voici un code exemple pour un composant de carousel :
   ```html
   <!-- components/carousel/carousel.html -->
    <div class="carousel">
        {% for slide in slides %}
            <div class="slide">{{ slide }}</div>
        {% endfor %}
    </div>
   ```
   ```javascript
    // components/carousel/carousel.js
    document.querySelectorAll('.carousel').forEach(carousel => {
        // Code pour faire bouger le carousel
    });
    ```
    ```python
    # components/carousel/carousel.py
    context.update({
        'slides': ['Slide 1', 'Slide 2', 'Slide 3']
    })
    ```
4. **Le programme détectera automatiquement le nouveau composant** et l'affichera dans la liste des composants disponibles.

## 🛠️ Personnalisation
- Ajoutez vos propres **composants** dans le dossier `components/`.
- Modifiez `base.html` pour personnaliser le design global.
- Ajoutez des styles supplémentaires avec Tailwind CSS.

## ✅ TODO List
- [x] Créer un projet Django
- [x] Générer des pages et composants
- [x] Copier les fichiers des composants
- [x] Créer des templates HTML dynamiques
- [x] Générer des routes et vues Django
- [x] Créer un menu de navigation
- [x] Utiliser Tailwind CSS pour le design
- [ ] Permettre la creation de sql pour le fichier si besoin 
- [ ] Ajouter des composants de base a voir les quels
- [ ] Permettre une page admin
- [ ] Si page admin alors sql pour tout compenent modifiable en admin
- [ ] Mettre les components dans un git - comment faire l'implementation
- [ ] Ajouter des tests unitaires - globaux et par composant si fourni]


## 📢 Contribution
Toute amélioration ou suggestion est la bienvenue ! 🚀

## 📄 Licence
Ce projet est sous licence **MIT**.

