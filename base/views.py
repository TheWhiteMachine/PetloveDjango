from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .models import Post, Coment, Mascota

from django.contrib import messages


def loginPage(request):
    context = {}
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Datos validados")
                return redirect('/')

        messages.error(request, "Datos incorrectos")

    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')


def registerPage(request):
    if (request.method == "POST"):
        username = request.POST.get("username")
        name = request.POST.get("name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            redirect('/registro')
        User.objects.create_user(
            username=username, email=email, first_name=name, last_name=last_name, password=password)
        return redirect('/login')
    return render(request, 'register.html')


def home(request):
    posts = Post.objects.order_by("-created")
    return render(request, 'home.html', {'posts': posts})


def mis_mascotas(request):
    pets = Mascota.objects.order_by("-created")
    return render(request, 'home.html', {'pets': pets})


def pet(request, id=None):

    if request.method == 'POST':
        id = request.POST.get('id')
        if (id is None):
            Mascota.objects.create(
                nombre=request.POST.get('nombre'),
                especie=request.POST.get('especie'),
                user=request.user,
                f_nacimiento=request.POST.get("f_nacimiento"),
                foto=request.POST.get("foto"),
                colores=request.POST.get("colores"),
                personalidad=request.POST.get("personalidad"),
                extras=request.POST.get("extras"),
                en_adopcion=request.POST.get("en_adopcion")


            )
            messages.success(request, "Registraste una nuvea Mascota")
            return redirect("/")
        else:
            m = Mascota.objects.get(id=id)
            if (p.user == request.user):
                m.nombre = request.POST.get('nombre'),
                m.especie = request.POST.get('especie'),
                m.user = request.user,
                m.f_nacimiento = request.POST.get("f_nacimiento"),
                m.foto = request.POST.get("foto"),
                m.colores = request.POST.get("colores"),
                m.personalidad = request.POST.get("personalidad"),
                m.extras = request.POST.get("extras"),
                m.en_adopcion = request.POST.get("en_adopcion"),
                m.save()

    context = {}
    if id is not None:
        p = Mascota.objects.get(id=id)
        context['mascota'] = m
    return render(request, 'pet.html', context)


def post(request, id=None):
    if request.method == 'POST':
        id = request.POST.get('id')
        if (id is None):
            Post.objects.create(
                title=request.POST.get('title'),
                text=request.POST.get('text'),
                user=request.user
            )
            messages.success(request, "Publicaste un nuveo post")
            return redirect("/")
        else:
            p = Post.objects.get(id=id)
            if (p.user == request.user):
                p.title = request.POST.get('title')
                p.text = request.POST.get('text')
                p.save()

    context = {}
    if id is not None:
        p = Post.objects.get(id=id)
        context['post'] = p
    return render(request, 'post.html', context)


def coment(request):
    p = Post.objects.get(id=request.POST.get('post'))
    Coment.objects.create(
        text=request.POST.get('text'),
        user=request.user,
        post=p

    )
    return redirect('/')
