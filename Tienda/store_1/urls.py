from django.urls import path
from . import views

urlpatterns = [
 path('cliente-list/', views.clienteList.as_view()),
 path('clientes-detail/<int:pk>/', views.clienteDetail.as_view()),
 path('categoria-list/', views.categoriaList.as_view()),
 path('categoria-detail/<int:pk>/', views.categoriaDetail.as_view()),
 path('producto-list/', views.productoList.as_view()),
 path('producto-detail/<int:pk>/', views.productoDetail.as_view()),
 path('dueño-list/', views.dueñoList.as_view()),
 path('dueño-detail/<int:pk>/', views.dueñoDetail.as_view()),
 path('users/', views.UserList.as_view()),
 path('users/<int:pk>/', views.UserDetail.as_view()),
]