from django import forms
from communitymanager.models import *


class SubForm(forms.Form):
    suivre = forms.BooleanField(widget=forms.HiddenInput(),required=False)
    nom = forms.IntegerField(widget=forms.HiddenInput(),required=False)

class CommentaireForm(forms.Form):
    commenter = forms.CharField(strip=True,widget=forms.Textarea,required=True)


class MyPostForm(forms.Form):
    titre = forms.CharField(max_length=100, strip=True,required=True)
    priorite = forms.CharField(max_length=50, required=True)
    description = forms.CharField(strip=True, required=True)
    commu = forms.CharField(max_length=50,required=True)
    envenementiel = forms.BooleanField(required=False)
    date_evenement = forms.DateTimeField(input_formats= ['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M'],required=False)

    def clean(self):
        cleaned_data = super(MyPostForm, self).clean()

        try:
            c = Communaute.objects.get(nom=cleaned_data.get('commu'))
        except Communaute.DoesNotExist :
            self.add_error("commu", "Cette communaute n'existe pas..")


        if self.cleaned_data.get('envenementiel') and self.cleaned_data.get('date_evenement')==None:
            self.add_error("date_evenement","Veuillez renseigner la date de l'evenement")
        return self.cleaned_data
