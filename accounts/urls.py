from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    
    path("lista-usuario",views.UserList.as_view() , name='lista_usuario'),
    path("detalle-usuario/<pk>",views.UserDetail.as_view() , name='detalle_usuario'),
    path("crea-usuario",views.UserCreate.as_view() , name='crear_usuario'),
    path("editar-usuario/<pk>",views.UserUpdate.as_view() , name='editar_usuario'),
    path("eliminar-usuario/<pk>",views.UserDelete.as_view() , name='eliminar_usuario'),
    
 
]
