from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_page(request):
  logout(request)
  return redirect('/') # redireciona para a pagina inicial
