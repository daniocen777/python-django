from importlib.resources import path
from django.urls import path

from inmuebleslist_app.views import inmueble_list
from inmuebleslist_app.views import inmueble_detalle

urlpatterns = [
    path('list/', inmueble_list, name='inmueble-list'),
    # buscar por id
    path('<int:id>', inmueble_detalle, name='inmueble-detalle'),
    
]
