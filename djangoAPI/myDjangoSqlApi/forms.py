from django import forms
from .models import *


class ProfForm(forms.ModelForm):
    class Meta:
        model = Prof
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = "__all__"
