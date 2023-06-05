from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from.models import Parc,Inscription
from django import forms

class InscriptionForm(ModelForm):
    class Meta:
        model = models.Inscription
        fields = ('nom', 'prenom', 'age', 'telephone','parc')
        labels = {
        'nom' : _('nom'),
        'prenom' : _('prenom'),
        'age' : _('age'),
        'telephone' : _('telephone'),
        'parc' : _('parc'),
        }

class ParcForm(ModelForm):
    class Meta:
        model = models.Parc
        fields = ('nom',)
        labels = {
        'nom' : _('nom')
        }