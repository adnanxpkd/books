from django import forms
from home.models import Audiobook, Ebook

class ConatctForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = '__all__'


class AudioBookForm(forms.ModelForm):
    class Meta:
        model = Audiobook
        fields = '__all__'