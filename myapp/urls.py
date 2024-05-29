from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('sign-up/',views.sign_up,name='sign-up'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('profile/',views.profile,name='profile'),
    path('add_product/',views.add_product,name='add_product'),
    path('show_product/',views.show_product,name='show_product'),
    path('edit_product/<int:pk>/',views.edit_product,name='edit_product'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('back/',views.back,name='back'),
    path('customer/',views.customer,name='customer'),
    path('quot/<int:pk>/',views.quot,name='quot'),



    
    
]