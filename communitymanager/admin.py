from django.contrib import admin
from .models import *
from django.utils.text import Truncator

# Register your models here.


class CommunauteAdmin(admin.ModelAdmin):
    list_display    = ('nom', )
    list_filter     = ('date_creation', 'abonnes')
    date_hierarchy  = 'date_creation'
    ordering        = ('date_creation', )
    search_fields    = ('nom','abonnes__username',)

    #fields = ('nom', )


class PrioriteAdmin(admin.ModelAdmin):
    list_display     = ('label',)
    search_fields    = ('label', )


class PostAdmin(admin.ModelAdmin):
    list_display    = ('titre', 'truncDescription', 'auteur', 'date_creation')
    list_filter     = ('priorite', 'date_creation', 'evenementiel', 'date_evenement', 'communaute')
    date_hierarchy  = 'date_creation'
    ordering        = ('date_creation',)
    search_fields   = ('titre', 'description','auteur__username')

    prepopulated_fields = {'slug': ('titre','auteur'), }
    fieldsets = (
        ('Paramètres Generaux', {
            'classes': ['wide', ],
            'fields' : ('titre', 'slug', 'auteur', 'communaute', 'priorite')
        }),
        ('Contenu du Post', {
            'classes': ['wide',],
            'fields' : ('description',)
        }),
        ('Evenement', {
            'classes': ['wide', ],
            'fields': ('evenementiel', 'date_evenement')
        }),
    )

    def truncDescription(self, post):
        return Truncator(post.description).chars(100, truncate='...')
    truncDescription.short_description = 'Aperçu du post'



class CommentaireAdmin(admin.ModelAdmin):
    list_display    = ('auteur', 'truncContenu', 'date_creation')
    list_filter     = ('auteur', 'post', 'date_creation', 'likes')
    date_hierarchy  = 'date_creation'
    ordering        = ('date_creation',)
    search_fields   = ('auteur__username', 'contenu', 'post__titre')

    fieldsets = (
        ('Paramètres Generaux', {
            'classes': ['wide', ],
            'fields' : ('auteur', 'post')
        }),
        ('Contenu du Commentaire', {
            'classes': ['wide',],
            'fields' : ('contenu',)
        }),
    )

    def truncContenu(self, commentaire):
        return Truncator(commentaire.contenu).chars(60, truncate='...')
    truncContenu.short_description = 'Contenu'


admin.site.register(Communaute, CommunauteAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Priorite, PrioriteAdmin)
admin.site.register(Commentaire, CommentaireAdmin)


