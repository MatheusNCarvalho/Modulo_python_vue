# coding: utf-8

from rest_framework import serializers
from .models import DadosPessoais
from .models import Marca
from .models import Produto
from .models import Funcionario
from .models import Cargo
from .models import Usuario
 #Classes responsáveis pela tradução dos dados na recepsão ou envio de dados via JSON.
class DadosPessoaisSerializer(serializers.ModelSerializer):
    class Meta:
        # classe que que terão seus dados serializados
        model = DadosPessoais
        depth = 1
        #atributos da classe Dados pessoais na models.py

        fields = ['id', 'name', 'adress', 'city', 'cep', 'phone', 'mobile']


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        depth = 1
        fields = ['id','nome', 'categoria']

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        depth = 1
        fields = ['id','descricao', 'preco', 'fkMarca']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        depth = 1
        fields = ['id','nome', 'email', 'cpf', 'telefone', 'celular', 'fkCargo']


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        depth = 1
        fields = ['id','nome', 'descricao']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        depth = 1
        fields = ['id','nome', 'email', 'usuario', 'senha']