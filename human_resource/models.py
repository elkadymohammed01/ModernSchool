from __future__ import unicode_literals
from django.db import models


class UserType(models.Model):
    type = models.CharField(max_length=30)

    class Meta:
        verbose_name = "دور الفرد"
        verbose_name_plural = "دور الفرد"

    def __str__(self):
        return self.type


class Level(models.Model):
    level = models.CharField(max_length=55)

    class Meta:
        verbose_name = ' المستوي'
        verbose_name_plural = ' المستوي'

    def __str__(self):
        return self.level


class Subject(models.Model):
    subject = models.CharField(max_length=55)
    is_required = models.BooleanField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="subject")

    class Meta:
        verbose_name = 'المادة'
        verbose_name_plural = 'المادة'

    def __str__(self):
        return self.subject


class Class(models.Model):
    class_name = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'الفصل'
        verbose_name_plural = 'الفصل'

    def __str__(self):
        return self.class_name


class Person(models.Model):
    name = models.CharField(max_length=70)
    barth_day = models.DateField()
    phone = models.CharField(max_length=13)
    type = models.ForeignKey(UserType, on_delete=models.CASCADE, related_name="user")

    class Meta:
        verbose_name = 'الاشخاص'
        verbose_name_plural = 'الاشخاص'

    def __str__(self):
        return self.name


class Student(Person):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="student")
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="student")

    class Meta:
        verbose_name = 'الطلاب'
        verbose_name_plural = 'الطلاب'

    def __str__(self):
        return self.name


class Parent(Person):
    children = models.ManyToManyField(Student, related_name="parent")
    levels = models.ManyToManyField(Level, related_name="parent")

    class Meta:
        verbose_name = 'الاباء'
        verbose_name_plural = 'الاباء'

    def __str__(self):
        return self.name


class Teacher(Person):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teacher')
    classes_name = models.ManyToManyField(Class, related_name="teacher")
    levels = models.ManyToManyField(Level, related_name="teacher")

    class Meta:
        verbose_name = 'المعلمين'
        verbose_name_plural = 'المعلمين'

    def __str__(self):
        return self.name


class Result(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="result")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="result")
    year = models.IntegerField()
    degree = models.FloatField()

    class Meta:
        verbose_name = 'النتائج'
        verbose_name_plural = 'النتائج'

    def __str__(self):
        return " نتيجة الطالب "+self.student.name+" لمادة "+self.subject.subject+" في المستوي "+self.subject.level.level
