# bache/urls.py

from django.urls import path, include
from . import views
from .views import mapa_baches, upzs_por_localidad, barrios_por_upz
from .routers import router
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('', views.index, name="inicio"),
    path('crear/', views.crear_bache, name='crear_bache'),  # <- Ya no fallará
    path('somos/', views.somos, name="somos"),
    path('sesion/', views.sesion, name="sesion"),
    path('mapa/', mapa_baches, name='mapa-baches'),
    path('ajax/upzs/', views.cargar_upzs, name='ajax_cargar_upzs'),
    path('ajax/barrios/', views.cargar_barrios, name='ajax_cargar_barrios'),
    path('api/', include(router.urls)),
    path('api/upzs-por-localidad/<int:localidad_id>/', upzs_por_localidad, name='upzs-por-localidad'),
    path('api/barrios-por-upz/<int:upz_id>/', barrios_por_upz, name='barrios-por-upz'),
    path('consultar/', views.ver_filtrado_baches, name='ver_filtrado_baches'),
    path('ajax/filtrar_baches/', views.filtrar_baches, name='filtrar_baches_ajax'),
    path('ajax/obtener_filtros/', views.obtener_filtros, name='obtener_filtros'),

    path('modificar_bache/', views.modificar_bache, name='modificar_bache'),
    path('ajax/modificar_bache/<str:id_bache>/', views.modificar_bache_post, name='modificar_bache_post'),  # POST AJAX
    path('ajax/get_bache/<str:id_bache>/', views.get_bache, name='get_bache'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
