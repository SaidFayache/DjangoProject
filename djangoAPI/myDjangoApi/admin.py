from django.contrib import admin
from .models import Prof, Student, Class, Subject, Note
# Register your models here.

admin.site.register(Prof)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Note)
