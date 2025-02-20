import os, shutil, subprocess

PROJECT_NAME = input("Nom du projet Django (par défaut 'generated_site'): ").strip() or "generated_site"
APP_NAME = "main"
RACINE = os.getcwd()
BASE_DIR = os.path.join(os.getcwd(), PROJECT_NAME)
TEMPLATES_DIR = os.path.join(BASE_DIR, APP_NAME, "templates")
COMPONENTS_DIR = os.path.join(TEMPLATES_DIR, "components")
COMPONENTS_PYTHON_DIR = os.path.join(RACINE, "components")

def get_all_components():
    components_dir = os.path.join(RACINE, "components")
    if not os.path.exists(components_dir):
        os.makedirs(components_dir)  # Crée le dossier s'il n'existe pas

    components = {}
    for folder in os.listdir(components_dir):
        folder_path = os.path.join(components_dir, folder)
        if os.path.isdir(folder_path):  # Vérifie que c'est un dossier
            components[folder] = folder_path  # Associe le nom du composant à son chemin
    return components

# Génère automatiquement ALL_COMPONENTS
ALL_COMPONENTS = get_all_components()

def get_user_input():
    num_pages = int(input("Combien de pages souhaitez-vous créer ? "))
    pages = []
    components_list = list(ALL_COMPONENTS.keys())
    string = "".join([f"{i+1} {components_list[i]}\n" for i in range(len(components_list))])
    for i in range(num_pages):
        page_name = input(f"Nom de la page index: " if i == 0 else f"Nom de la page {i+1}: ").strip().lower() 
        print("Choisissez les composants pour cette page :" + string)
        components = [int(c) for c in input("Entrez les composants séparés par une virgule : ").split(",")]
        pages.append({"name": page_name, "components": [components_list[c - 1] for c in components if c <= len(components_list) and c > 0]})
    return pages

def create_django_project():
    subprocess.run(["django-admin", "startproject", PROJECT_NAME], check=True)
    os.chdir(BASE_DIR)
    subprocess.run(["python3", "manage.py", "startapp", APP_NAME], check=True)
    
    settings_path = os.path.join(BASE_DIR, PROJECT_NAME, "settings.py")
    with open(settings_path, "r") as f:
        settings_content = f.read()
    
    if "'main'" not in settings_content:
        settings_content = settings_content.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    'main',")
        with open(settings_path, "w") as f:
            f.write(settings_content)
    
    print("Django project and app created successfully.")


def copy_selected_files(src_folder, dest_folder, file_name):
    """Copie uniquement les fichiers spécifiés d'un dossier source vers un dossier destination."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    src_file = os.path.join(src_folder, file_name)
    dest_file = os.path.join(dest_folder, file_name)
    print(f"📁 Fichier source : {src_file}")
    print(f"📁 Dossier destination : {dest_folder}")

    if os.path.exists(src_file):
        shutil.copy2(src_file, dest_file)
        print(f"✅ {file_name} copié vers {dest_folder}")
    else:
        print(f"⚠️ {file_name} non trouvé dans {src_folder}")

def copy_component_templates(site_structure):
    """Génère les templates des composants et copie uniquement certains fichiers sélectionnés."""
    os.makedirs(COMPONENTS_DIR, exist_ok=True)

    menu_code = ""
    for site in site_structure:
        menu_code += f"""
            <li>
                <a href="{{% url '{site['name']}' %}}" class="text-white hover:text-gray-300 px-4 py-2 block">
                    {site['name'].capitalize()}
                </a>
            </li>
        """

    dest_path = os.path.join(COMPONENTS_DIR, "menu.html")
    with open(dest_path, "w") as f:
        f.write(f"""
        <nav class="bg-blue-600 shadow-md">
            <div class="container mx-auto">
                <ul class="flex space-x-4 p-4">
                    {menu_code}
                </ul>
            </div>
        </nav>
        """)

    # Fichiers spécifiques à copier pour chaque composant
    files_to_copy = [".html", ".js"]

    print(site_structure)
    liste_components = [] 
    for page in site_structure:
        for component in page['components']:
            if component not in liste_components:
                liste_components.append(component)
                for file_to_copy in files_to_copy:
                    dest_folder = os.path.join(COMPONENTS_DIR, component)
                    src_folder = os.path.join(RACINE, "components", component)
                    print(f"📁 Copie des fichiers pour le composant {component + file_to_copy}...")
                    print(f"📁 Dossier source : {src_folder}")
                    if os.path.exists(src_folder):
                        copy_selected_files(src_folder, dest_folder, component + file_to_copy)
                    else:
                        print(f"⚠️ Le composant {component} n'existe pas dans {src_folder}")
                print("✅ Component templates copied/created successfully.")

def create_base_template():
    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    base_html_path = os.path.join(TEMPLATES_DIR, "base.html")
    
    base_html_content = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
        <title>{% block title %}Mon Site{% endblock %}</title>
    </head>
    <body class="bg-gray-100 text-gray-900 font-sans w-full min-h-screen ">
        <header class="bg-blue-600 text-white py-4 shadow-md">
            <div class="container mx-auto px-4">
                {% include 'components/menu.html' %}
            </div>
        </header>
        <main class="container mx-auto px-4 py-8">
            {% block content %}{% endblock %}
        </main>
        <footer class="bg-gray-800 text-white py-4 mt-8 shadow-md text-center text-sm">
            <div class="container mx-auto text-center">
                <p>&copy; 2025 - Mon Site</p>
            </div>
        </footer>
        <script>
            {% block scripts %}{% endblock %}
        </script>
    </body>
</html>
    """
    
    with open(base_html_path, "w") as f:
        f.write(base_html_content)
    
    print("Base template created successfully.")

def load_components(page):
    components = {
        "python_components": "",
        "html_components": "",
        "js_components": ""
    }
    for component in page['components']:
        # python
        py_file = os.path.join(COMPONENTS_PYTHON_DIR, component, f"{component}.py")

        if os.path.exists(py_file):
            with open(py_file, "r") as f:
                code = f.read()
            components["python_components"] += "\n".join([f"    {line}" for line in code.split("\n")])

        html_file = os.path.join(COMPONENTS_DIR, component, f"{component}.html")
        if os.path.exists(html_file):
            components["html_components"] += f"\n\t{{% include 'components/{component}/{component}.html' %}}"
            
        js_file = os.path.join(COMPONENTS_DIR, component, f"{component}.js")
        if os.path.exists(js_file):
            components["js_components"] += f"\n\t{{% include 'components/{component}/{component}.js' %}}"
        if components["python_components"] != "":
            components["python_components"] = f"{components['python_components']}\n"
    return components




def create_views_and_templates(site_structure):
    views_path = os.path.join(BASE_DIR, APP_NAME, "views.py")
    urls_path = os.path.join(BASE_DIR, PROJECT_NAME, "urls.py")
    os.makedirs(TEMPLATES_DIR, exist_ok=True)

    views_content = """
from django.shortcuts import render

"""
    urls_content = f"""
from django.urls import path
from {APP_NAME} import views
    
urlpatterns = [
"""

    i = 0
    for page in site_structure:
        page_name = page['name']
        components = load_components(page)

        views_content += f"""
def {page_name}_view(request):
    context = {{}}
{components['python_components']}
    return render(request, '{page_name}.html', context=context)
"""
        if i == 0:
            urls_content += f"    path('', views.{page_name}_view, name='{page_name}'),\n"
            i += 1
        else:
            urls_content += f"    path('{page_name}/', views.{page_name}_view, name='{page_name}'),\n"

        with open(os.path.join(TEMPLATES_DIR, f"{page_name}.html"), "w") as f:
            f.write(f"""
{{% extends 'base.html' %}}
{{% block content %}}
    {components["html_components"]}
{{% endblock %}}
{{% block scripts %}}
    {components["js_components"]}
{{% endblock %}}""")

    urls_content += "]\n"

    with open(views_path, "w") as f:
        f.write(views_content)

    with open(urls_path, "w") as f:
        f.write(urls_content)

    print("Views, URLs, and templates created successfully.")

def main():
    site_structure = get_user_input()
    create_django_project()
    copy_component_templates(site_structure)
    create_base_template()
    create_views_and_templates(site_structure)
    
    print("Django site generation complete! Run `python3 manage.py runserver` to start the server.")
    
    subprocess.run(["python3", "manage.py", "runserver"], check=True)

if __name__ == "__main__":
    main()
