from .user import UserSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .autor import AutorSerializer
from .livro import LivroListSerializer, LivroDetailSerializer, LivroSerializer,LivroRetrieveSerializer,LivroAlterarPrecoSerializer,LivroAjustarEstoqueSerializer
from .compra import CompraSerializer, CompraCreateUpdateSerializer, ItensCompraSerializer,CompraListSerializer,ItensCompraListSerializer
from .favoritos import FavoritosSerializer