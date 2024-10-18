from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Página principal
    path('personas/', views.lista_personas, name='lista_personas'),
    path('<int:persona_id>/', views.detalle_persona, name='detalle_persona'),
    path('crear/', views.crear_persona, name='crear_persona'),
    path('<int:persona_id>/editar/', views.editar_persona, name='editar_persona'),
    path('<int:persona_id>/eliminar/', views.confirmar_eliminar_persona, name='eliminar_persona'),  # Cambia a la vista de confirmación
]
