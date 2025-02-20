if request.method == "POST":
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")

    # Traitement ou sauvegarde des données
    print(f"Message reçu de {name} ({email}) : {message}")
    
    context.update({
        "messages": [
            {"message": "Votre message a bien été envoyé !", "tag": "success"},
        ],
    })
