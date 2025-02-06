from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from core.models import Favorito, Livro
from core.serializers import FavoritosSerializer
from rest_framework.permissions import IsAuthenticated

class FavoritosViewSet(ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritosSerializer
    permission_classes = [IsAuthenticated]  # Garante que apenas usuários autenticados acessem

    def create(self, request, *args, **kwargs):
        """Adiciona um livro aos favoritos"""
        livro_id = request.data.get("livro_id")
        favoritos_id = request.data.get("favoritos")

        if not livro_id or not favoritos_id:
            return Response({"error": "Campos 'livro_id' e 'favoritos' são obrigatórios."},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            livro = Livro.objects.get(id=livro_id)
            favoritos = Favorito.objects.get(id=favoritos_id)
        except Livro.DoesNotExist:
            return Response({"error": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        except Favorito.DoesNotExist:
            return Response({"error": "Favoritos não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        item_favorito, created = Favorito.objects.get_or_create(
            livro=livro
        )

        if not livro_id:
            return Response({"error": "O campo 'livro_id' é obrigatório."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            livro = Livro.objects.get(id=livro_id)
        except Livro.DoesNotExist:
            return Response({"error": "Livro não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Obtém ou cria a lista de favoritos do usuário autenticado
        favoritos, created = Favorito.objects.get_or_create(usuario=request.user)

        # Adiciona o livro aos favoritos do usuário se ainda não estiver na lista
        if not favoritos.livros.filter(id=livro.id).exists():
            favoritos.livros.add(livro)
            return Response({"message": "Livro adicionado aos favoritos."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Livro já está nos favoritos."}, status=status.HTTP_200_OK)
