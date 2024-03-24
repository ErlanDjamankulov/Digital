from django.urls import path, include
from .views import *

urlpatterns = [
         path('accounth/', include('allauth.urls')),

         path('category/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='category_list'),
         path('category/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='category_detail'),
         path('status/', StatusViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='status_list'),
         path('status/<int:pk>/', StatusViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='status_detail'),
         path('clients/', ClientsViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='clients_list'),
         path('clients/<int:pk>/', ClientsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='clients_detail'),
         path('flats/', FlatsViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='flats_list'),
         path('flats/<int:pk>/', FlatsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='flats_detail'),
         path('manager/', ManagerViewSets.as_view({'get': 'list', 'post': 'create'}),
                name='manager_list'),
         path('manager/<int:pk>/', ManagerViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
                name='manager_detail'),
]