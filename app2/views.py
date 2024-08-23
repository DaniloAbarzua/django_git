from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(resquest):
    return HttpResponse("<h1> Soy el index de la APP2</h1>")

def contenido(request):
    html="""
        <p>Soy el parrafo de la app2.</p>
        <h2> soy un subtitulo de la app2</h2>
    """
    return HttpResponse(html)