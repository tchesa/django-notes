from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Note

def list_note_page(request):
  notes = Note.objects.all()
  context = {'notes': notes}
  return render(request, 'notes.html', context)

def view_note_page(request, id):
  note = Note.objects.get(id = id)
  context = {'note': note}
  return render(request, 'view.html', context)
