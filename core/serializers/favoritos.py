from rest_framework import serializers
from core.models import Favorito, Livro  # Importando Livro corretamente
from core.serializers.livro import LivroSerializer  # Certifique-se de que esse serializer existe

class FavoritosSerializer(serializers.ModelSerializer):
    livro = LivroSerializer(read_only=True)  # Serializa os detalhes do livro
    livro_id = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all(), source="livro", write_only=True)

    class Meta:
        model = Favorito
        fields = ["id", "livro", "livro_id"]
