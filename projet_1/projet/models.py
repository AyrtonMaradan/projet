from django.db import models

# Create your models here.


class Parc(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        chain = f"{self.nom} fait partis de la liste des parcs."
        return chain

    def dico(self):
        return {"nom":self.nom}

class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(blank=True,null=True)
    telephone = models.CharField(max_length=20)
    parc = models.ForeignKey(Parc, on_delete=models.CASCADE)
    accompagné = models.BooleanField(blank=True,null=True)

    def __str__(self):
        chain = f"{self.nom} à acheter le billet n°{self.id}. Pour le contacter veuillez appeler le {self.telephone }"
        return chain

    def dico(self):
        return {"nom":self.nom, "prenom":self.prenom,"age":self.age, "telephone":self.telephone, "parc": self.parc}


