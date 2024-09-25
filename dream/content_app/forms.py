from django import forms

from .models import FAQModel, NewsUpdateModel, AboutModel


class FAQForm(forms.ModelForm):
    model = FAQModel
    fields = '__all__'


class NewsUpdateForm(forms.ModelForm):
    model = NewsUpdateModel
    fields = '__all__'


class AboutForm(forms.ModelForm):
    model = AboutModel
    fields = '__all__'
