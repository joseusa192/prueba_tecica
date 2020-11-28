from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    Dueño = serializers.PrimaryKeyRelatedField(many=True, queryset=Dueño.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'Dueño']

class DueñoSerializer(ModelSerializer):

    class Meta:
        model = Dueño
        fields = '__all__'
        owner = serializers.ReadOnlyField(source='owner.username')


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def create(self, validated_data):
        return Cliente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nom_Cliente = validated_data.get('nom_Cliente', instance.nom_Cliente)
        instance.tel_Cliente = validated_data.get('tel_Cliente', instance.tel_Cliente)
        instance.correo_Cliente = validated_data.get('correo_Cliente', instance.correo_Cliente)
        instance.save()
        return instance


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = CategoriasProductos
        fields = '__all__'

        def create(self, validated_data):
            return CategoriasProductos.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.nom_Categoria = validated_data.get('nom_Categoria', instance.nom_Categoria)
            instance.save()

            return instance


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def create(self, validated_data):
        return Producto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nom_Producto = validated_data.get('nom_Producto', instance.nom_Producto)
        instance.pre_Producto = validated_data.get('pre_Producto', instance.pre_Producto)
        instance.ven_Realizada = validated_data.get('ven_Realizada', instance.ven_Realizada)
        instance.uni_St_Producto = validated_data.get('uni_St_Producto', instance.uni_St_Producto)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.save()

        return instance
