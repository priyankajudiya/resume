from django import forms
from django.db.models import fields
from . import models

#Profile form
class profileForm(forms.ModelForm):
    class Meta:
        model = models.profile
        fields = '__all__'

#Education form
class educationForm(forms.ModelForm):
    class Meta:
        model = models.education
        fields = '__all__'

#skils
class skilsForm(forms.ModelForm):
    class Meta:
        model = models.skils
        fields = '__all__'

#Contact Form
class contactForm(forms.ModelForm):
    class Meta:
        model = models.contact
        fields = '__all__'