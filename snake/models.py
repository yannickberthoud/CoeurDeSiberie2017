# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

class Family(models.Model):
    """ Schémas DB des familles de serpents """
    name = models.CharField(max_length = 256, verbose_name = "Nom")
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Famille"
        verbose_name_plural = "Familles"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Family, self).save(*args, **kwargs)

class Mutation(models.Model):
    """ Schémas DB des mutations """
    name = models.CharField(max_length = 256)

    def __str__(self):
        return self.name

class Snake(models.Model):
    """ Schémas DB des serpents """
    SEX_CHOICES = (
        ('M', 'Mâle'),
        ('F', 'Femelle'),
        ('D', 'Mâle et femelle'),
        ('I', 'Inconnu')
    )
    parent_m = models.CharField(max_length = 256, verbose_name = "Reproducteur", blank = True)
    parent_f = models.CharField(max_length = 256, verbose_name = "Reproductrice", blank = True)
    family = models.ForeignKey(Family, on_delete = models.CASCADE, verbose_name = "Famille")
    s_name = models.CharField(max_length = 256, verbose_name = "Nom scientifique")
    c_name = models.CharField(max_length = 256, verbose_name = "Nom commun")
    birthday = models.CharField(max_length = 10, verbose_name = "Né le")
    mutation = models.ForeignKey(Mutation, on_delete = models.CASCADE)
    sex = models.CharField(max_length = 1, verbose_name = "Sexe", choices = SEX_CHOICES)
    slug = models.SlugField()
    captive_birth = models.BooleanField(verbose_name = "NZ", blank = True)
    cites = models.BooleanField(verbose_name = "Soumi au CITES", blank = True)

    for_sale = models.BooleanField(verbose_name = "À vendre", blank = True)
    price_sale = models.FloatField(verbose_name = "Prix de vente", blank = True, null = True)
    price_cpl = models.FloatField(verbose_name = "Prix de couple", blank = True, null = True)
    flex_price = models.BooleanField(verbose_name = "Prix à discuter", blank = True)

    old = models.BooleanField(verbose_name = "Ancien serpent", blank = True)
    infos = models.TextField(verbose_name = "Informations complémentaires", blank = True)
    private_data = models.TextField(verbose_name = "Informations pour nous", blank = True)

    def __str__(self):
        return self.family.name +" " + self.s_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.s_name)
        super(Snake, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Serpent"
        verbose_name_plural = "Nos serpents"

class Gallery(models.Model):
    image = models.ImageField(verbose_name = "Nom", upload_to='snakes')
    snake = models.ForeignKey(Snake, on_delete = models.CASCADE, related_name = "snakesg", related_query_name = "snakeg")

    class Meta:
        verbose_name = "Média"
        verbose_name_plural = "Médias"

    def __str__(self):
        return self.image.path