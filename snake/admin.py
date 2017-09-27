# -*- coding: utf-8 -*-
from django.contrib import admin
from snake.models import Family, Mutation, Snake, Gallery 

class PhotoInline(admin.StackedInline):
    model = Gallery
    extra = 1


class FamilyAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    search_fields = ['name']
    ordering = ['name']


class MutationAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    search_fields = ['name']
    ordering = ['name']

class SnakeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Parents', {'fields':['parent_m', 'parent_f']}),
        ('Idendité', {'fields':['family', 's_name', 'c_name', 'birthday']}),
        ('Mutation & sexe', {'fields':['mutation', 'sex']}),
        ('Loi', {'fields':['captive_birth', 'cites']}),
        ('Vendre', {'fields':['for_sale', 'price_sale', 'price_cpl', 'flex_price']}),
        ('Informations complémentaires', {'fields':['infos', 'old']}),
        ('Status pour nous', {'fields':['private_data',]})
    ]
    inlines = [PhotoInline]
    list_filter = ['family', 'sex', 'for_sale']
    list_display = ('id', 'family', 'parent_m', 'parent_f', 's_name','c_name', 'sex', 'captive_birth', 'cites', 'for_sale', 'price_sale', 'price_cpl', 'flex_price')
    search_fields = ['id', 'parent_m', 'parent_f', 'family', 's_name', 'c_name']
    ordering = ['s_name']


admin.site.register(Family, FamilyAdmin)
admin.site.register(Mutation, MutationAdmin)
admin.site.register(Snake, SnakeAdmin)