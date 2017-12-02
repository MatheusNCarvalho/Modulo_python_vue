# coding: utf-8
from django.http import Http404
from rest_framework.decorators import api_view

from .serializer import DadosPessoaisSerializer, FuncionarioSerializer, CargoSerializer

from .models import DadosPessoais, Funcionario, Cargo

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
