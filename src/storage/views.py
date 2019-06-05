from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Note

def note_detail_page(request, slug):
  obj = get_object_or_404(Note, slug=slug)
  template_name = 'note_detail.html'
  context = {'object': obj}
  return render(request, template_name, context)
