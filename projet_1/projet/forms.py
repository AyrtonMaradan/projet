from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from.models import Parc,Inscription
from django import forms

class InscriptionForm(ModelForm):
    class Meta:
        model = models.Inscription
        fields = ('nom', 'prenom', 'date_de_naissance', 'telephone','parc','accompagné')
        labels = {
        'nom' : _('nom'),
        'prenom' : _('prenom'),
        'date_de_naissance' : _('date_de_naissance'),
        'telephone' : _('telephone'),
        'parc' : _('parc'),
        'accompagné': _('accompagné'),
        }

class ParcForm(ModelForm):
    class Meta:
        model = models.Parc
        fields = ('nom',)
        labels = {
        'nom' : _('nom')
        }