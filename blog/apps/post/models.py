from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40, null=False, blank=False)
    activado=models.BooleanField(default=True)
    fecha_creacion=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Categorias'
    def __str__(self):
        return str(self.nombre)
class Post(models.Model):
    id=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100, null=False, blank=False)
    resumen=models.CharField(max_length=500, null=False, blank=False)
    texto=models.TextField(max_length=5000, null=False, blank=False)
    imagen=models.ImageField(upload_to='post', null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado=models.BooleanField(default=True)
    fecha_creacion=models.DateField(auto_now_add=True)
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural='Posteos'
    def __str__(self):
        return str(self.titulo)
class Comentario(models.Model):
	usuario = models.ForeignKey(User, on_delete = models.CASCADE)
	texto = models.TextField(max_length = 1000)
	posteo = models.ForeignKey(Post, on_delete = models.CASCADE)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.texto)

