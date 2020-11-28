from django.db import models


# Create your models here.

class Dueño(models.Model):
    nomDueño= models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='Dueño', on_delete=models.CASCADE)
    highlighted = models.TextField()

class CategoriasProductos(models.Model):
    nom_Categoria = models.CharField(max_length=30, unique=True)
    cod_Categoria = models.AutoField(primary_key=True)


class Producto(models.Model):
    cod_Producto = models.AutoField(primary_key=True)
    nom_Producto = models.CharField(max_length=30)
    pre_Producto = models.IntegerField(default=0)
    ven_Realizada = models.BooleanField(default=False)
    uni_St_Producto = models.IntegerField(default=0)
    categoria = models.ForeignKey(CategoriasProductos, null=False, blank=False, on_delete=models.CASCADE)


class Cliente(models.Model):
    nom_Cliente = models.CharField(max_length=80)
    tel_Cliente = models.CharField(max_length=15)
    correo_Cliente = models.EmailField(max_length=100)
    ID_dni = models.AutoField(primary_key=True)

