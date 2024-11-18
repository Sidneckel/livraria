from rest_framework import serializers
from core.models import Livro
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from uploader.models import Image
from uploader.serializers import ImageSerializer

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
        capa_attachment_key = SlugRelatedField(
            source="capa",
            queryset=Image.objects.all(),
            slug_field="attachment_key",
            required=False,
            write_only=True,
            
    )
        capa = ImageSerializer(
            required=False,
            read_only=True
    )
class LivroDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class LivroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autores']  

class LivroListRetrieveSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)