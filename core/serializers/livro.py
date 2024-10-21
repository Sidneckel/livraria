from rest_framework import serializers
from core.models import Livro

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1
class LivroDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1