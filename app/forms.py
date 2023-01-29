from django import forms
from .models import CiscoSwitch

class CiscoSwitchForm(forms.ModelForm):
    class Meta:
        model = CiscoSwitch
        fields = ('device_type', 'host', 'username', 'password')