from rest_framework import serializers

from .models import *


class ProfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prof
        fields = ('profId', 'fullname')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('studentId', 'fullname', 'classId')


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = ('classId', 'className')


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ('subjectId', 'classId', 'profId', 'subjectName')


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('noteId', 'studentId', 'subjectId', 'mark')
