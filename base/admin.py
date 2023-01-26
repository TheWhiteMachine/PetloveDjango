from django.contrib import admin

# Register your models here.

from .models import Post, Coment, Mascota, Mensajes, Adopciones

admin.site.register(Post)
admin.site.register(Coment)
admin.site.register(Mascota)
admin.site.register(Mensajes)
admin.site.register(Adopciones)

