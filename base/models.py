from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Coment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


class Mascota(models.Model):
    nombre = models.CharField(max_length=200, null=False, blank=False)
    especie = models.CharField(
        max_length=150, null=False, blank=False, default="no")
    raza = models.CharField(max_length=100, null=False, blank=False)
    f_nacimiento = models.DateField(null=False, blank=False)
    foto = models.ImageField(upload_to="mascotas", null=True)
    colores = models.TextField()
    personalidad = models.TextField(max_length=300)
    extras = models.TextField(max_length=150, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    en_adopcion = models.CharField(max_length=2, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Mensajes(models.Model):
    asunto = models.CharField(max_length=150, default="asunto")
    text = models.TextField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    destinatario = models.TextField()

    def __str__(self):
        return self.asunto


class Adopciones(models.Model):
    titulo = models.CharField(max_length=150)
    mascota = models.ForeignKey(Mascota, null=True, on_delete=models.SET_NULL)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(max_length=200)

    def __str__(self):
        return self.titulo
