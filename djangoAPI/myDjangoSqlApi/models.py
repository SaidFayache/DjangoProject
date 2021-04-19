from django.db import models


class Prof(models.Model):
    profId = models.UUIDField()
    fullname = models.CharField(max_length=60)

    class Meta:
        db_table = "prof"


class Student(models.Model):
    studentId = models.UUIDField()
    fullname = models.CharField(max_length=60)
    classId = models.UUIDField()

    class Meta:
        db_table = "student"


class Class(models.Model):
    classId = models.UUIDField()
    className = models.CharField(max_length=60)

    class Meta:
        db_table = "class"


class Subject(models.Model):
    subjectId = models.UUIDField()
    classId = models.UUIDField()
    profId = models.UUIDField()
    subjectName = models.CharField(max_length=60)

    class Meta:
        db_table = "subject"


class Note(models.Model):
    noteId = models.UUIDField()
    studentId = models.UUIDField()
    subjectId = models.UUIDField()
    mark = models.FloatField()

    class Meta:
        db_table = "note"

