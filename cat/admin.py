from django.contrib import admin
from .models import Color, Cat, Gallery


class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 1

class CatAdmin(admin.ModelAdmin):
    """ Définition de l'interface administrateur """
    fieldsets = [
        ('Parenté', {'fields': ['parent_m', 'parent_f', 'name', 'los_number']}),
        ('Informations', {'fields': ['color', 'sex', 'birthday']}),
        ('Ventes & Saillie', {'fields': ['for_sale', 'price_sale', 'for_jut', 'jut_price', 'previous_jut_birth']}),
        ('Informations complémentaires', {'fields': ['informations',]})

    ]
    exclude = ('slug',)
    inlines = [GalleryInline]
    list_display = 'name', 'los_number', 'color', 'birthday'
    ordering = ['name']


admin.site.register(Cat, CatAdmin)
admin.site.register(Color)