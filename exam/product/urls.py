from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('normal/', views.normal, name='normal'),
    path('faq/', views.faq, name='faq'),
    path('product/<int:id>/', views.product, name='product'),
]
