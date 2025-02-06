from django.db import models
from .livro import Livro
from .user import User

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="itens_favoritos")

    def __str__(self):
        return f"{self.livro.titulo}"
