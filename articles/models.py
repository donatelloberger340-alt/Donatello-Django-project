from django.db import models


class Article(models.Model):
    titre = models.CharField(
        max_length=200,
        verbose_name="Nom du produit"
    )

    auteur = models.CharField(
        max_length=100,
        verbose_name="Auteur"
    )
    resume = models.TextField(
        verbose_name="Résumé"
    )

    contenu = models.TextField(
        verbose_name="Description complète"
    )

    image = models.ImageField(
    upload_to="products/",
    verbose_name="Image du produit",
    blank=True,
    null=True
    )

    date_publication = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titre