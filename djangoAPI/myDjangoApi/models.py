from django.db import models


class Prof(models.Model):
    profId = models.UUIDField()
    fullname = models.CharField(max_length=60)

    def __str__(self):
        return self.fullname


class Student(models.Model):
    studentId = models.UUIDField()
    fullname = models.CharField(max_length=60)
    classId = models.UUIDField()

    def __str__(self):
        return self.fullname


class Class(models.Model):
    classId = models.UUIDField()
    className = models.CharField(max_length=60)

    def __str__(self):
        return self.className


class Subject(models.Model):
    subjectId = models.UUIDField()
    classId = models.UUIDField()
    profId = models.UUIDField()
    subjectName = models.CharField(max_length=60)

    def __str__(self):
        return self.subjectName


class Note(models.Model):
    noteId = models.UUIDField()
    studentId = models.UUIDField()
    subjectId = models.UUIDField()
    mark = models.FloatField()

    def __str__(self):
        return self.mark
