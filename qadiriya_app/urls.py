from django.urls import path
from . import views 
urlpatterns = [ 
    path('', views.dashboard , name = 'dashboard'), 
    path('abdul-qadir/', views.abdulqadir , name='abdul-qadir'), 
    path('uwesu-ahmad/', views.uwesuAhmad , name = 'uwesu-ahmad'),
    path('mohd-nasor/', views.mohdNasor , name = 'mohd-nasor'), 
    path('tawasuli-kubwa/', views.tawasuliKubwa , name = 'tawasuli-kubwa'), 
    path('fatha-mashekhe/', views.fathaMashekhe , name = 'fatha-mashekhe'),         
]