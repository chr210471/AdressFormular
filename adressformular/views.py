from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Adresse


# 1. View für das Adressformular
def adressformular(request):
    return render(request, 'adressformular.html')


# 2. View zum Speichern der Adresse (API-Endpunkt)
def adresse_speichern(request):
    if request.method == 'POST':
        strasse = request.POST.get('strasse')
        hausnummer = request.POST.get('hausnummer')
        plz = request.POST.get('plz')
        ort = request.POST.get('ort')
        bundesland = request.POST.get('bundesland')

        # Speichern der Adresse in der Datenbank
        adresse = Adresse.objects.create(
            strasse=strasse,
            hausnummer=hausnummer,
            plz=plz,
            ort=ort,
            bundesland=bundesland
        )
        return JsonResponse({'status': 'success', 'message': 'Adresse gespeichert!'})
    return JsonResponse({'status': 'error', 'message': 'Ungültige Anfrage'}, status=400)


# 3. View zur Anzeige aller gespeicherten Adressen
def adressen_anzeigen(request):
    adressen = Adresse.objects.all()
    return render(request, 'adressen_anzeigen.html', {'adressen': adressen})
