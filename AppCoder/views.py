from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso= Curso (nombre="Desarrollo WEB", camada= 19881)
    curso.save()
    documentoDetexto=f"----> Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse (documentoDetexto)