from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Note
from .forms import NoteModelForm


@login_required
def list_note_page(request):
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes}
    return render(request, 'notes.html', context)


@login_required
def view_note_page(request, id):
    note = Note.objects.get(id=id)
    context = {'note': note}
    return render(request, 'view.html', context)


@login_required
def new_note_page(request):
    form = NoteModelForm(request.POST or None)  # tenta receber a requisição POST
    if form.is_valid():
        obj = form.save()  # salva o objeto
        obj.user = request.user
        obj.save()
        return redirect('/')  # redireciona para a pagina inicial
    return render(request, 'new.html', {"form": form})


@login_required
def edit_note_page(request, id):
    note = Note.objects.get(id=id)
    form = NoteModelForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()  # salva o objeto
        return redirect('/')  # redireciona para a pagina inicial
    return render(request, 'edit.html', {'form': form})


# @login_required
# def upload_note(id):
#     def upload(request):
#         if request.method == 'POST':
#             handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
#             return HttpResponse("Successful")
#     # note = Note.objects.get(id=id)
#     # filename = note.title.replace(' ', '_') + ".txt"
#     # content = note.content
#     # response = HttpResponse(content, content_type='text/plain')
#     # response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
#     # return response
#
#
# def handle_uploaded_file(file, filename):
#     for s in file.read().split(','):
#         myobject = output(fileData=s)
#         myobject.save()


@login_required
def download_note(id):
    note = Note.objects.get(id=id)
    filename = note.title.replace(' ', '_') + ".txt"
    content = note.content
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response


@login_required
def delete_note_page(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect('/')  # redireciona para a pagina inicial
