from django import forms
from .models import Contact


class stform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"