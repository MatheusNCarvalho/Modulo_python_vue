# coding: utf-8
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

# importação das classes do arquivo views.py
from portfolios.views import FuncionarioListAndPost, FuncionarioById, CargoListAndPost, CargoById, \
    MarcaListAndPost, MarcaById, ProdutoListAndPost, ProdutoById, UsuarioListAndPost, UsuarioById

helper_patterns = [
    # Mapeamento e roteamento para acesso as funcionalidades do sistema.
    # Urls para as classes que contem os metodos de Get, Post, Put e Delete.

    url(r'^marcas/$', MarcaListAndPost.as_view()), # acesso aos metodos de get e post de marcas
    url(r'^marcas/(?P<pk>[0-9]+)/$', MarcaById.as_view()), # acesso aos métodos de get, post, put e delete passando o id.

    url(r'^produtos/$', ProdutoListAndPost.as_view()),
    url(r'^produtos/(?P<pk>[0-9]+)/$', ProdutoById.as_view()),

    url(r'^funcionarios/$', FuncionarioListAndPost.as_view()),
    url(r'^funcionarios/(?P<pk>[0-9]+)/$', FuncionarioById.as_view()),

    url(r'^cargos/$', CargoListAndPost.as_view()),
    url(r'^cargos/(?P<pk>[0-9]+)/$', CargoById.as_view()),

    url(r'^usuarios/$', UsuarioListAndPost.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', UsuarioById.as_view())


]

urlpatterns = format_suffix_patterns(helper_patterns)
