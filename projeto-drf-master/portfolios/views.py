# coding: utf-8
from django.http import Http404
from rest_framework.decorators import api_view

from .serializer import DadosPessoaisSerializer, MarcaSerializer, ProdutoSerializer, FuncionarioSerializer, CargoSerializer, UsuarioSerializer

from .models import DadosPessoais, Marca, Produto, Funcionario, Cargo, Usuario

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

''' class PortfolioListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
'''

'''class PortfolioView(APIView):
    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)
'''

'''class FuncionarioView(APIView):
    serializer_class = FuncionarioSerializer

    # GET com argumentos
    def get(self, request, pk, format=None):
        funcionario = Funcionario.objects.get(pk=pk)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    def get(self, request, format=None):
        serializer = self.serializer_class(Funcionario.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
'''

# Classe view responsável pelos metodos Get e Post da model Cargo
class CargoListAndPost(APIView):
    # Implementação do serializador dos dados
    serializer_class = CargoSerializer

    # realizando o get, enviando todos os dados armazenados no banco
    def get(self, request, format=None):
        # pega os dados serializados da model Cargo
        serializer = self.serializer_class(Cargo.objects.all(), many=True)
        # envia via JSON os dados para o requisitante
        return Response(serializer.data)

    # realizando o post, recebendo os dados do front-end
    def post(self, request, format=None):
        # recebe dos dados serialializados através do Post que o front-end envia
        serializer = self.serializer_class(data=request.data)
        # validação do serializer
        if serializer.is_valid():
            # envia os dados para o serializer realizar a tradução e salvar na model
            serializer.save()
            # envia via JSON os dados que foram armazenados e o status da operação
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class CargoById(APIView):
    serializer_class = CargoSerializer

    def get_object(self, pk):
        try:
            # retorna a chave do cargo
            return Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            raise Http404

    # get com argumentos
    def get(self, request, pk, format=None):

        # recebe a chave do objeto
        cargo = self.get_object(pk)
        # recebe o Cargo filtrado pela chave primaria
        serializer = CargoSerializer(cargo)
        # envia para o front-end o cargo selecionado
        return Response(serializer.data)

    # realizando o put
    def put(self, request, pk, format=None):

        cargo = self.get_object(pk)
        # recebe os dados, informando a chave
        serializer = self.serializer_class(cargo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # realizando o delete
    def delete(self, request, pk, format=None):

        cargo = self.get_object(pk)
        # deleta o objeto passando a chave
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MarcaListAndPost(APIView):
    serializer_class = MarcaSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Marca.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class MarcaById(APIView):
    serializer_class = MarcaSerializer

    def get_object(self, pk):
        try:
            return Marca.objects.get(pk=pk)
        except Marca.DoesNotExist:
            raise Http404

    # GET com argumentos
    def get(self, request, pk, format=None):

        marca = self.get_object(pk)

        serializer = MarcaSerializer(marca)
        return Response(serializer.data)

    # REALIZANDO O PUT
    def put(self, request, pk, format=None):

        marca = self.get_object(pk)

        serializer = self.serializer_class(marca, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        marca = self.get_object(pk)

        marca.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProdutoListAndPost(APIView):
    serializer_class = ProdutoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Produto.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class ProdutoById(APIView):
    serializer_class = ProdutoSerializer

    def get_object(self, pk):
        try:
            return Produto.objects.get(pk=pk)
        except Produto.DoesNotExist:
            raise Http404

    # GET com argumentos
    def get(self, request, pk, format=None):

        produto = self.get_object(pk)

        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    # REALIZANDO O PUT
    def put(self, request, pk, format=None):

        produto = self.get_object(pk)

        serializer = self.serializer_class(produto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        produto = self.get_object(pk)

        produto.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FuncionarioListAndPost(APIView):
    serializer_class = FuncionarioSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Funcionario.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class FuncionarioById(APIView):
    serializer_class = FuncionarioSerializer

    def get_object(self, pk):
        try:
            return Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            raise Http404

    # GET com argumentos
    def get(self, request, pk, format=None):

        funcionario = self.get_object(pk)

        serializer = ProdutoSerializer(funcionario)
        return Response(serializer.data)

    # REALIZANDO O PUT
    def put(self, request, pk, format=None):

        funcionario = self.get_object(pk)

        serializer = self.serializer_class(funcionario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        funcionario = self.get_object(pk)

        funcionario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UsuarioListAndPost(APIView):
    serializer_class = UsuarioSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Usuario.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class UsuarioById(APIView):
    serializer_class = UsuarioSerializer

    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404

    # GET com argumentos
    def get(self, request, pk, format=None):

        usuario = self.get_object(pk)

        serializer = ProdutoSerializer(usuario)
        return Response(serializer.data)

    # REALIZANDO O PUT
    def put(self, request, pk, format=None):

        usuario = self.get_object(pk)

        serializer = self.serializer_class(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        usuario = self.get_object(pk)

        usuario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

