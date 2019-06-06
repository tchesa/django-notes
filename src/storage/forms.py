from django import forms

class NoteForm (forms.Form):
  title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Título'}))
  content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Conteúdo'}), label='')
