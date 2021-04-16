from django.core import serializers
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import ProfSerializer
from .models import Prof
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def profGetAdd(request):
    if request.method == 'GET':
        queryset = Prof.objects.all()
        serializer = ProfSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)