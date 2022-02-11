from __future__ import unicode_literals

from django.db.models import *
from django.shortcuts import render
from importlib import import_module
from ..models import *
from .forms import AddStudent


def students_home(request):
    form = AddStudent()
    result = []
    students = []
    if request.GET:
        get_request = request.GET
        Student(name=get_request['name'], barth_day=get_request['age'],
                phone=get_request['phone'], type_id=get_request['type'],
                class_name_id=get_request['class_name'], level_id=get_request["level"]) \
            .save()
    if request.POST:
        students = Student.objects.order_by('result__year', 'result__degree').all()
        name = request.POST['name']
        level = request.POST['level']
        class_name = request.POST['class_name']
        if len(name) > 0:
            pass
        if level != '0':
            students = students.filter(level=level)
        if class_name != '0':
            students = students.filter(class_name=class_name)
        for student in students:
            result_student = student.result.all()
            number_of_subject = student.result.all().count()
            total_result = 0.0
            for result_subject in result_student:
                total_result += result_subject.degree
            if number_of_subject > 0:
                total_result /= number_of_subject
            result.append(total_result)
        result.reverse()
    context = {'form': form, 'students': students,
               'result': result,
               'class_at_level': get_students_by_level_and_class(),
               'first_student': get_first_student_in_every_level(),
               'percentage': get_percentage_of_students()}
    return render(request, "students/add.html", context)


def get_students_by_level_and_class():
    level_class_students = Student.objects.values('level').annotate(Count('id')).all()
    student_levels_list = []
    icons = ['bxl-baidu', 'bxl-audible', 'bxl-blender', 'bxl-react', 'bxl-deviantart', 'bx-key',
             'bxl-discourse', 'bxl-drupal', 'bxl-docker', 'bxl-firefox', 'bxl-jquery', 'bx-infinite']
    index = 0
    for class_at_level in level_class_students:
        result = {}
        result['level'] = class_at_level['level']
        result['count'] = class_at_level['id__count']
        result['icon'] = icons[index % len(icons)]
        index += 1
        student_levels_list.append(result)
    return student_levels_list


def get_first_student_in_every_level():
    first_students_in_levels = Student.objects \
        .values('id', 'name', 'level__level', 'class_name__class_name') \
        .annotate(Avg('result__degree'))
    result_by_level = {}
    head_of_student = []
    for level in Level.objects.all():
        result_by_level[level.level] = {'degree': 0}
    for student in first_students_in_levels:
        if student['result__degree__avg'] is not None \
                and result_by_level[student['level__level']]['degree'] < student['result__degree__avg']:
            result_by_level[student['level__level']]['degree'] = int(student['result__degree__avg'])
            result_by_level[student['level__level']]['name'] = student['name']
            result_by_level[student['level__level']]['id'] = student['id']
            result_by_level[student['level__level']]['class'] = student['class_name__class_name']
            result_by_level[student['level__level']]['level'] = student['level__level']

    for item in result_by_level.values():
        head_of_student.append(item)
    print(head_of_student)
    return head_of_student


def get_percentage_of_students():
    list_degree = [0, 50, 60, 70, 80, 90]
    list_max_degree = [50, 60, 70, 80, 90, 100]
    list_degree_title = ['very Bad', 'Bad', 'Good', 'Very Good', 'Excellent', 'Magic']
    all_student = Student.objects.all().count()
    list_of_result = []
    for index in range(len(list_degree)):
        result = {}
        result['count'] = Result.objects.filter(degree__gte=list_degree[index])\
            .exclude(degree__gte=list_max_degree[index]).count()
        result['title'] = list_degree_title[index]
        result['percentage'] = (result['count']*100)/all_student
        list_of_result.append(result)
    return list_of_result
