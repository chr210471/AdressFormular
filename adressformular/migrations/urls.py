"""
URL configuration for WienerAdressen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .. import views
from ..views import adressformular

adressformular()
from django.contrib import admin
from django.urls import path

urlpatterns = [
path('formular/', views.adressformular, name='adressformular'),  # URL für das Adressformular
    path('adresse_speichern/', views.adresse_speichern, name='adresse_speichern'),  # URL für den API-Endpunkt zum Speichern der Adresse
    path('adressen/', views.adressen_anzeigen, name='adressen_anzeigen'),  # URL für die Übersicht der Adressen
    path('admin/', admin.site.urls),
]
