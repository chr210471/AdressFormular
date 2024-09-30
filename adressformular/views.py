# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from adressformular.models import Adresse

# View für das Adressformular
def adressformular(request):
    return render(request, 'adressformular/adressformular.html')

# API zum Speichern der Adressen
def adresse_speichern(request):
    if request.method == 'POST':
        strasse = request.POST.get('strasse')
        hausnummer = request.POST.get('hausnummer')
        plz = request.POST.get('plz')
        ort = request.POST.get('ort')
        # Speichern der Daten in die Datenbank
        Adresse.objects.create(strasse=strasse, hausnummer=hausnummer, plz=plz, ort=ort)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

# Anzeigen der Adressen
def adressen_anzeigen(request):
    adressen = Adresse.objects.all()
    return render(request, 'adressformular/adressuebersicht.html', {'adressen': adressen})

