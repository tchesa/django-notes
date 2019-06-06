from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Note

def main_page(request):
  notes = Note.objects.all()
  print(notes)
  template_name = 'index.html'
  context = {'notes': notes}
  return render(request, template_name, context)
