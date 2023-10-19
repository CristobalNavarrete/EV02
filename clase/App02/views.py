from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def App02(request):
    

    return render(request,'App/App.html')
    

def Chile(request):
    data={
         "titulo":"Chile",
           "dato01":" En Chile tienen el desierto más árido del planeta.",
         "dato02":" Las momias más antiguas del mundo se encontraron en el norte de Chile",
         "dato03":" El partido de fútbol más largo del mundo se jugó en Chile",
         "dato04":" La Luna fue inscrita por un chileno",
         'imagen':'imagenes/chile.png'
        }
    return render(request,'App/App.html',data)

def EEUU(request):
    data={
         "titulo":"EEUU",
           "dato01":" La bandera fue diseñada por un estudiante de 16 años: Robert G. Heft ",
         "dato02":" Celebrar la navidad fue considerado un acto ilegal: Antes de 1907 en Estados unidos ",
         "dato03":" La rosa es la flor nacional",
         "dato04":" Estados unidos ha tenido en total 9 capitales",
         'imagen':'imagenes/EEUU.png'
        }
    return render(request,'App/App.html',data)
def Brasil(request):
    data={
         "titulo":"Brasil",
          "dato01":" Brasil ocupa el quinto lugar en términos de población",
         "dato02":" El deporte nacional de Brasil es el fútbol",
         "dato03":" La bebida de café más deliciosa se prepara en Brasil",
         "dato04":" No hay religión oficial en este país",
         'imagen':'imagenes/brazil.png'
        }
    return render(request,'App/App.html',data)

def Peru(request):
    data={
         "titulo":"Peru",
         "dato01":"El Perú es el tercer país más grande de Sudamérica",
         "dato02":"Cuenta con un territorio de: 1,285,216 km²",
         "dato03":"La palabra “Perú” proviene de una tribu panameña llamada “Biru”",
         "dato04":"Cusco significa “Ombligo del mundo”",
         'imagen':'imagenes/Peru.png'
        }
    return render(request,'App/App.html',data)