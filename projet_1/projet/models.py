from django.db import models

# Create your models here.


class Parc(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        chain = f"{self.nom} à été ajouter à la BDD"
        return chain

    def dico(self):
        return {"nom":self.nom}

class Inscription(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.DateField(blank=True,null=True)
    telephone = models.CharField(max_length=20)
    parc = models.ForeignKey(Parc, on_delete=models.CASCADE)

    def __str__(self):
        chain = f"{self.nom} à acheter le billet n°{self.id}. Pour le contacter veuillez appeler le {self.telephone }"
        return chain

    def dico(self):
        return {"nom":self.nom, "auteur":self.prenom,"age":self.age, "telephone":self.telephone, "Parc": self.Parc}


