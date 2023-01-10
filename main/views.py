from django.shortcuts import render
from django.http import JsonResponse

def clientes(request):
    if request.method == 'GET':
        return JsonResponse(clientes)