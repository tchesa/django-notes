from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'signup.html', args)


def logout_page(request):
    logout(request)
    return redirect('/')  # redireciona para a pagina inicial
