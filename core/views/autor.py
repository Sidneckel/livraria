from rest_framework.viewsets import ModelViewSet
from core.models import Autor
from core.serializers import AutorSerializer
from core.views.livro import LivroViewSet

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
