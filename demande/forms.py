from django import forms
from demande.models import Demande


class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = "__all__"
