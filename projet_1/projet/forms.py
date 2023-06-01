from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
class InscriptionForm(ModelForm):
    class Meta:
        model = models.Inscription
        fields = ('nom', 'prenom', 'age', 'telephone')
        labels = {
        'nom' : _('nom'),
        'prenom' : _('prenom') ,
        'age' : _('age'),
        'telephone' : _('telephone')
        }