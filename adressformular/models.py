from django.db import models

# Create your models here.


from django.db import models

class Adresse(models.Model):
    strasse = models.CharField(max_length=100)
    hausnummer = models.CharField(max_length=10)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=50)
    bundesland = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.strasse} {self.hausnummer}, {self.plz} {self.ort}, {self.bundesland}'
