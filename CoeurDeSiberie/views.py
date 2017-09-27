from django.shortcuts import render
from django.views.generic import ListView, DetailView

def home(request):
    return render(request, 'CoeurDeSiberie/home.html')


def contact(request):
    if request.method == "GET":
        return render(request, 'CoeurDeSiberie/contact.html')
    if request.method == "POST":
        name = request.POST['name']
        from_email = request.POST['email']
        subject = 'coeur-de-siberie.ch - nouveau message  ' + name + " <" + from_email + ">"
        comment = request.POST['comment']
        if name and from_email and comment:
            try:
                send_mail(subject, comment, from_email, ['info@coeur-de-siberie.ch',])
                messages.add_message(request, messages.SUCCESS, 'Votre message nous est bien parvenu. Nous vous répondrons dans les plus brefs délais.')
            except BadHeaderError:
                messages.add_message(request, messages.ERROR, 'Une erreur s\'est produite, veuillez réessayer.Si l\'erreur persiste, veuillez nous joindre à inf                                                                                                                                   o@coeur-de-siberie.ch.')
                return render(request, 'CoeurDeSiberie/contact.html')
        else:
            messages.add_message(request, messages.ERROR, 'Une erreur s\'est produite. Tous les champs sont obligatoires.')
            return render(request, 'CoeurDeSiberie/contact.html')
        return render(request, 'CoeurDeSiberie/contact.html')