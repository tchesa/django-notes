from django import forms
from .models import Note


class NoteModelForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Título', 'maxLength': 120}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Digite sua nota'}), label='')

    class Meta:
        model = Note
        fields = ['title', 'content']
