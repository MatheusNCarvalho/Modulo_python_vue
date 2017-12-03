# coding: utf-8
from django.http import Http404
from rest_framework.decorators import api_view

from .serializer import DadosPessoaisSerializer, MarcaSerializer, ProdutoSerializer, FuncionarioSerializer, CargoSerializer, UsuarioSerializer

from .models import DadosPessoais, Marca, Produto, Funcionario, Cargo, Usuario

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from django.shortcuts import render


# Codigo do projeto antigo


def portfolio_exibir(request):
    pessoa = DadosPessoais.objects.all()
    context = {'pessoa': pessoa}

    return render(request, 'portfolios/portfolio_exibir.html', context)


'''
-- Primeiro Código --
class PortfolioListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)
'''

'''
 -- Segundo Código --

class PortfolioListView(APIView):
    serializer_class = DadosPessoaisSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(DadosPessoais.objects.all(), many=True)
        return Response(serializer.data)


class PortfolioView(APIView):

    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)


'''


class PortfolioListView(APIView):
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


class PortfolioView(APIView):
    def get(self, request, pk, format=None):
        user = DadosPessoais.objects.get(pk=pk)
        serializer = DadosPessoaisSerializer(user)
        return Response(serializer.data)


class FuncionarioView(APIView):
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


class CargoListAndPost(APIView):
    serializer_class = CargoSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Cargo.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)


class CargoById(APIView):
    serializer_class = CargoSerializer

    def get_object(self, pk):
        try:
            return Cargo.objects.get(pk=pk)
        except Cargo.DoesNotExist:
            raise Http404

    # GET com argumentos
    def get(self, request, pk, format=None):

        cargo = self.get_object(pk)

        serializer = CargoSerializer(cargo)
        return Response(serializer.data)

    # REALIZANDO O PUT
    def put(self, request, pk, format=None):

        cargo = self.get_object(pk)

        serializer = self.serializer_class(cargo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):

        cargo = self.get_object(pk)

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
        serializer = self.serializer_class(UsuarioSerializer.objects.all(), many=True)
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

