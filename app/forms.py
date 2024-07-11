from django import forms
from . import models
from .models import Comand, User
from .models import Profile

from .models import Purchase
# forms.py
# forms.py
class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '60'}))
    name2 = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '60'}))
    name3 = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '60'}))
    name4 = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '60'}))
    name5 = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '60'}))
    comandname = forms.CharField(widget=forms.TextInput(attrs={'class':'textarea', 'size': '60'}))
    class Meta:
        model = models.Comand
        fields = ['name', 'name2', 'name3', 'name4', 'name5', 'comandname']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['time', 'name', 'item_count']

    def clean_time(self):
        # Проверяем, свободно ли выбранное время
        time = self.cleaned_data['time']
        if Purchase.objects.filter(time=time).exists():
            raise forms.ValidationError("Это время уже занято. Пожалуйста, выберите другое время.")
        return time



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img', 'name', 'bio']  # Add other fields here