# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .students_affairs.forms import AddStudent
from .models import *


def home_page(request):
    form = AddStudent()
    return render(request, "home.html", {'form': form})

