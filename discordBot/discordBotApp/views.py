from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
# from rest_framework.response import Response


# Create your views here.


class Discord_Bot_View(generic.View):
    def get(self, request, format=None, *args, **kwargs):
        bauti = 'hola'
        return JsonResponse({"name": bauti})
