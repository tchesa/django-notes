"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
  1. Add an import: from my_app import views
  2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
  1. Add an import: from other_app.views import Home
  2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
  1. Import the include() function: from django.urls import include, path
  2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from storage.views import (list_note_page, new_note_page, view_note_page, edit_note_page)
from .views import (home_page, about_page, contact_page)

urlpatterns = [
  path('', list_note_page),
  path('new/', new_note_page),
  path('<int:id>/', view_note_page),
  path('<int:id>/edit', edit_note_page)
]
