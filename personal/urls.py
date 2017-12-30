from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'asus/', views.asus, name='asus'),
	url(r'acer/', views.acer, name='acer'),
	url(r'lenovo/', views.lenovo, name='lenovo'),
]

