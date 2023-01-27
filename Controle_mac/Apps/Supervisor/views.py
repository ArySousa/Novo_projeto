from django.shortcuts import render
from django.http import HttpResponse


def supervisor(request):
    return HttpResponse('Bem Vindo a pagina de Supervisor')


def novo(request):
    return HttpResponse('Bem Vindo a pagina de Novo Cadastro')


def editar(request):
    return HttpResponse('Bem Vindo a pagina de Editar Cadastro')


def excluir(request):
    return HttpResponse('Bem Vindo a pagina de Excluir Cadastro')