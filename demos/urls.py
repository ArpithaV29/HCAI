from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from . import views

app_name = 'demos'

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('project1/', include('project1.urls')),
    path('', views.index, name='index'),
    path('upload/', views.upload_csv, name='upload'), 
    path('plot/', views.generate_plot, name='plot'), 
    path('generate-plot/', views.generate_plot_ajax, name='generate_plot_ajax'),
]



