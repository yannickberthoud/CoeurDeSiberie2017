# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

class Color(models.Model):
    """ Schemas de la base de données des colorations """
    name = models.CharField(max_length = 256)

    class Meta:
        verbose_name = "Coloration"
        verbose_name_plural = "Colorations"

    def __str__(self):
        return self.name

class Cat(models.Model):
    """ Schemas de la base de données des chats """
    SEX_CHOICES = (
        ('M', 'Mâle'),
        ('F', 'Femelle'),
        ('I', 'Inconnu')
    )
    parent_m = models.CharField(max_length = 256, verbose_name = "Reproducteur")
    parent_f = models.CharField(max_length = 256, verbose_name = "Reproductrice")
    name = models.CharField(max_length = 256)
    slug = models.SlugField()
    los_number = models.CharField(max_length = 256, verbose_name = "Numéro LOS")

    color = models.ForeignKey(Color, on_delete = models.CASCADE, verbose_name = "Couleur")
    sex = models.CharField(max_length = 1, verbose_name = "Sexe", choices = SEX_CHOICES)
    birthday = models.DateField(verbose_name = "Né le")

    for_sale = models.BooleanField(verbose_name = "À vendre", blank = True)
    price_sale = models.FloatField(verbose_name = "Prix de vente", blank = True)
    for_jut = models.BooleanField(verbose_name = "Pour saillie", blank = True)
    jut_price = models.FloatField(verbose_name = "Prix de la saillie", blank = True)

    previous_jut_birth = models.BooleanField(verbose_name = "Né d'une précédente saillie", blank = True)

    informations = models.TextField(verbose_name = "Informations complémentaire")

    class Meta:
        verbose_name = "Chat"
        verbose_name_plural = "Chats"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Cat, self).save(*args, **kwargs)

class Gallery(models.Model):
    image = models.ImageField(verbose_name = "Nom", upload_to='cats')
    cat = models.ForeignKey(Cat, on_delete = models.CASCADE, related_name = "cats", related_query_name = "catsg")

    class Meta:
        verbose_name = "Média"
        verbose_name_plural = "Médias"

    def __str__(self):
        return self.image.path