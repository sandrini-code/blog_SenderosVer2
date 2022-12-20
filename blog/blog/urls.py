"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
#from blog.apps.post import views
from apps.post.views import  crearPost, plantillaHija1, plantillaHija2, leerPost, comentar_Post
from apps.post.views import  blog, quienesSomos, formularioContacto, contactar, register, publicarPost
from apps.post.views import fauna, flora, hongos, proyectos, publicaciones, servicios
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static

#from blog.apps.post.views import publicarPost

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_post/', crearPost, name='crear_post'),
    path("plantillaHija1/", plantillaHija1),
    path("plantillaHija2/", plantillaHija2),
    path("", blog),
    path("quienesSomos/", quienesSomos),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar),
    path('register/', register, name='register'),
    path('auth/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('publicarPost/', publicarPost, name='publicarPost'),
    path('flora/', flora, name='flora'),
    path('fauna/', fauna, name='fauna'),
    path('hongos/', hongos, name='hongos'),
    path('proyectos/', proyectos, name='proyectos'),
    path('publicaciones/', publicaciones, name='publicaciones'),
    path('servicios/', servicios, name='servicios'),
    path('comentar/', comentar_Post, name='comentar'),
    re_path('leer_post/(?P<id>\d+)/$', leerPost, name='posteo'),
]
