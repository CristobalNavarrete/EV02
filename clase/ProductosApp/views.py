from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'templatesProductos/index.html')

def electronica(request):
    data={
         "titulo":"Electronica",
         'producto1':"mac",
         'producto2':"ceclucar",
         'producto3':"plolystation",
         'url':'/www.inacap.cl/',
         'imagen':'imagenes/producto.jpg' }
    return render(request,'templatesProductos/productos.html',data)

def juguetes(request):
    data={
         "titulo":"jugetes",
         'producto1':"juguete 1",
         'producto2':"jugete 2",
         'producto3':"jugete 3",
         'url':'/www.inacap.cl/',
         'imagen':'imagenes/producto.jpg'
        }
    return render(request,'templatesProductos/productos.html',data)

def ropa(request):
    data={
         "titulo":"ropa",
         'producto1':"rpoa 1",
         'producto2':"ropa 2",
         'producto3':"ropa 3",
         'url':'/www.inacap.cl/',
         'imagen':'imagenes/producto.jpg'
        }
    return render(request,'templatesProductos/productos.html',data)