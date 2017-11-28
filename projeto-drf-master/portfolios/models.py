# coding: utf-8
from django.db import models


class DadosPessoais(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')
    adress = models.CharField(max_length=100, verbose_name='Endereço')
    city = models.CharField(max_length=50, verbose_name='Cidade')
    cep = models.CharField(max_length=50, verbose_name='Cep')
    phone = models.CharField(max_length=20, verbose_name='Telefone')
    mobile = models.CharField(max_length=20, verbose_name='Celular')

    about = models.TextField(max_length=255, verbose_name='Sobre')
    data_nascimento = models.CharField(max_length=255, default='01 de janeiro de 2000', verbose_name='Data Nascimento')
    email = models.EmailField(verbose_name='Email')

    conhecimentos = models.TextField(max_length=255, verbose_name='Conhecimentos')
    github = models.CharField(max_length=100, default='http://github.com/SeuGit', verbose_name='Github')
    current_position = models.CharField(max_length=100, verbose_name='Cargo atual')
    empresa = models.CharField(max_length=100, verbose_name='Empresa')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Dados Pessoais'
        verbose_name_plural = 'Dados Pessoais'


class Marca(models.Model):
    nome = models.CharField(max_length=50, null=False)
    categoria = models.CharField(max_length=50, null=False)


def __str__(self):
    return self.name


class Meta:
    verbose_name = 'Dados Marcas'
    verbose_name_plural = 'Dados Marcas'


class Produto(models.Model):
    descricao = models.CharField(max_length=50, null=False)
    preco = models.FloatField(null=False)
    marca = models.ForeignKey(Marca)


def __str__(self):
    return self.nome

class Meta:
    verbose_name = 'Dados Produto'
    verbose_name_plural = 'Dados Produto'

class Cargo(models.Model):
    nome = models.CharField(max_length=50, null=False)
    descricao = models.CharField(max_length=255, null=False)


def __str__(self):
    return self.nome
class Meta:
    verbose_name = 'Dados Cargo'
    verbose_name_plural = 'Dados Cargo'


class Funcionario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null=False)
    celular = models.CharField(max_length=20, null=False)
    fkCargo = models.ForeignKey(Cargo)


def __str__(self):
    return self.nome
class Meta:
    verbose_name = 'Dados Funcionario'
    verbose_name_plural = 'Dados Funcionario'




class Usuario(models.Model):
    nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=255, null=False)
    usuario = models.CharField(max_length=50, null=False)
    senha = models.CharField(max_length=50, null=False)


data_alteracao = models.DateTimeField(null=False)


def __str__(self):
    return self.nome

class Meta:
    verbose_name = 'Dados Usuario'
    verbose_name_plural = 'Dados Usuario'
