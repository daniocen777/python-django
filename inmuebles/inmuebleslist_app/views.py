from django.shortcuts import render
from inmuebleslist_app.models import Inmueble
from django.http import JsonResponse

# Create your views here.


def inmueble_list(request):
    # Obtener toda la data
    inmuebles = Inmueble.objects.all()
    dictionary = {
        'inmuebles': list(inmuebles.values())
    }
    # Devolver en formato json
    return JsonResponse(dictionary)


def inmueble_detalle(request, id):
    inmueble = Inmueble.objects.get(pk=id)
    dictionary = {
        'direccion': inmueble.direccion,
        'pais': inmueble.pais,
        'imagen': inmueble.imagen,
        'activo': inmueble.activo,
        'descripcion': inmueble.descripcion,
    }
    # Devolver en formato json
    return JsonResponse(dictionary)
