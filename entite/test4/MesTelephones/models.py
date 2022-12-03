from django.db import models


class Telephone(models.Model):
    nom = models.CharField(max_length=30)
    realisateur = models.CharField(max_length=30)
    prix = models.FloatField()
    datedecreation = models.DateField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE,)

    def __str__(self) -> str:
    #    return self.libelle     
        return f"{self.nom} {self.type}"


class Type(models.Model):
    nomType = models.CharField(max_length=30)  
    description = models.TextField(null=True)    

    def __str__(self) -> str:
        return self.nomType 

