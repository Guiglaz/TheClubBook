from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Communaute(models.Model):
    nom = models.CharField(max_length=50)
    abonnes = models.ManyToManyField(User, related_name="abonnes")

    def __str__(self):
        return self.nom


class Priorite(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label


class Post(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(null=True)
    date_creation = models.DateTimeField(verbose_name='Date de publication', default=timezone.now)
    communaute = models.ForeignKey(Communaute, on_delete=models.CASCADE)
    priorite = models.ForeignKey(Priorite, on_delete=models.CASCADE)
    evenementiel = models.BooleanField(default=False)
    date_evenement = models.DateTimeField(verbose_name="Date de l'evenement", null=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} ecrit par {1}".format(self.titre, self.auteur)

    def addSlug(self):
        self.slug = self.slug.join(char for char in str(self) if char.isalnum())


class Commentaire(models.Model):
    date_creation = models.DateTimeField(verbose_name='Date du commentaire', default=timezone.now)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return "{0} a commente {1}".format(self.auteur, self.contenu)
