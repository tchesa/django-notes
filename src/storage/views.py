from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .models import Note
from .forms import NoteForm

def list_note_page(request):
  notes = Note.objects.all()
  context = {'notes': notes}
  return render(request, 'notes.html', context)

def view_note_page(request, id):
  note = Note.objects.get(id = id)
  context = {'note': note}
  return render(request, 'view.html', context)

def new_note_page(request):
  form = NoteForm(request.POST or None) # tenta receber a requisição POST
  if form.is_valid():
    obj = Note.objects.create(**form.cleaned_data) # cria o objeto
    return redirect('/') # redireciona para a pagina inicial
  return render(request, 'new.html', {"form": form})

def edit_note_page(request, id):
  note = Note.objects.get(id = id)
  context = {'note': note}
  return render(request, 'edit.html', context)
