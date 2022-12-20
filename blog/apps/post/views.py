from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Post, Categoria, Comentario
from .forms import PostForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import UserRegisterForm
#from Modulos.Academica.plantillas import *
from django.contrib import messages
from django.db.models import Q
from datetime import datetime


# Create your views here.
def plantillaHija1(request):
    return render(request, "plantillaHija1.html", {})
def fauna(request):
    fauna = Post.objects.filter(categoria__nombre="fauna").distinct()
    return render(request, "secciones/fauna.html", {"fauna": fauna})
def flora(request):
    flora = Post.objects.filter(categoria__nombre="flora").distinct()
    return render(request, "secciones/flora.html", {"flora": flora})
def hongos(request):
    hongos = Post.objects.filter(categoria__nombre="hongos").distinct()
    return render(request, "secciones/hongos.html", {"hongos": hongos})
def proyectos(request):
    proyectos = Post.objects.filter(categoria__nombre="proyectos").distinct()
    return render(request, "secciones/proyectos.html", {"proyectos":proyectos})
def publicaciones(request):
    publicaciones = Post.objects.filter(categoria__nombre="publicaciones").distinct()
    return render(request, "secciones/publicaciones.html", {"publicaciones":publicaciones})
def servicios(request):
    servicios = Post.objects.filter(categoria__nombre="servicios").distinct()
    return render(request, "secciones/servicios.html", {"servicios":servicios})

def plantillaHija2(request):
    return render(request, "secciones/plantillaHija2.html", {})
def blog(request):
    queryset = request.GET.get("buscar")
    cate = request.GET.get("categoria")
    fecha= request.GET.get("fecha")
    meses={"Enero":"01", "Febrero":"02", "Marzo":"03", "Abril":"04", "Mayo":"05", "Junio":"06", "Julio":"07", "Agosto":"08", "Septiembre":"09", "Octubre":"10", "Noviembre":"11", "Diciembre":"12"}
    for mes in meses:
        if mes == fecha:
            mes_Post=meses[mes]
    posts = Post.objects.filter(publicado=True)
    categ = Categoria.objects.all()
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(resumen__icontains=queryset) |
            Q(texto__icontains=queryset)
        ).distinct()
    elif cate and cate!= "Categorias":
        posts = Post.objects.filter(categoria__nombre=cate).distinct()
    elif fecha and fecha!= "Meses":
        posts = Post.objects.filter(
            Q(fecha_creacion__month=mes_Post),
        )

    context = {
        'posts': posts,
        'categorias': categ
    }
    return render(request, "blog.html", context)
def quienesSomos(request):
    return render(request, "quienesSomos.html", {})
def formularioContacto(request):
    return render(request,"formularioContacto.html")
def contactar(request):
    if request.method == "POST":
        asunto=request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/Email " + request.POST["txtEmail"]
        email_desde= settings.EMAIL_HOST_USER
        email_para=["gastonrg9@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
@login_required
@permission_required("staff")
def crearPost(request):
    if request.method=='POST':
        post_form=PostForm(request.POST or None, request.FILES or None)
        if post_form.is_valid():
            post_form.save()
            return redirect('crear_post')
    else:
        post_form=PostForm()
    return render(request,  'post/index.html',{'post_form':post_form})


def register (request):
    if request.method == 'POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f"Usuario {username} creado")
            return redirect(blog)
    else:
        form= UserRegisterForm()

    context={'form' : form}

    return render(request, 'register.html', context)

def publicarPost(request):
    posts= Post.objects.all()
    return render(request, "publicarPost.html", {'posts': posts})

def leerPost(request, id):
    if request.method=='GET':
        post = Post.objects.get(id=id)
        comentarios = Comentario.objects.filter(posteo=id)
        context = {
            'post': post,
            'comentarios': comentarios
        }
    return render(request, 'post/post.html', context)

@login_required
def comentar_Post(request):
    com = request.POST.get('comentario',None)
    usu = request.user
    noti = request.POST.get('id_post', None)
    post = Post.objects.get(id = noti)
    Comentario.objects.create(usuario = usu, posteo = post, texto = com)
    return redirect(reverse_lazy('posteo', kwargs={'id': noti}))