from django.core import serializers
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import *
from .models import *
from rest_framework.decorators import api_view

#TODO Chnage serializer to form & complete sql api 

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

@api_view(['DELETE','PATCH'])
def profEditDelete(request,pid):
    if request.method == 'DELETE':
        prof = Prof.objects.get(profId=pid)
        prof.delete()
        return Response('Prof deleted')
    elif request.method == 'PATCH':
        prof = Prof.objects.get(profId=pid)
        data = JSONParser().parse(request)
        serializer = ProfSerializer(data=data, instance=prof, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET','POST'])
def studentGetAdd(request):
    if request.method == 'GET':
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE','PATCH'])
def studentEditDelete(request, sid):
    if request.method == 'DELETE':
        student = Student.objects.get(studentId=sid)
        student.delete()
        return Response('Student deleted')
    elif request.method == 'PATCH':
        student = Student.objects.get(studentId=sid)
        data = JSONParser().parse(request)
        serializer = ProfSerializer(data=data, instance=student, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET','POST'])
def classGetAdd(request):
    if request.method == 'GET':
        queryset = Class.objects.all()
        serializer = ClassSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE','PATCH'])
def classEditDelete(request, cid):
    if request.method == 'DELETE':
        classe = Class.objects.get(classId=cid)
        classe.delete()
        return Response('Student deleted')
    elif request.method == 'PATCH':
        classe = Class.objects.get(classId=cid)
        data = JSONParser().parse(request)
        serializer = ClassSerializer(data=data, instance=classe, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET','POST'])
def subjectGetAdd(request):
    if request.method == 'GET':
        queryset = Subject.objects.all()
        serializer = SubjectSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE','PATCH'])
def subjectEditDelete(request, sid):
    if request.method == 'DELETE':
        subject = Subject.objects.get(subjectId=sid)
        subject.delete()
        return Response('Student deleted')
    elif request.method == 'PATCH':
        subject = Subject.objects.get(subjectId=sid)
        data = JSONParser().parse(request)
        serializer = SubjectSerializer(data=data, instance=subject, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET','POST'])
def noteGetAdd(request):
    if request.method == 'GET':
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE','PATCH'])
def noteEditDelete(request, nid):
    if request.method == 'DELETE':
        note = Note.objects.get(noteId=nid)
        note.delete()
        return Response('Student deleted')
    elif request.method == 'PATCH':
        note = Note.objects.get(noteId=nid)
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data, instance=note, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)