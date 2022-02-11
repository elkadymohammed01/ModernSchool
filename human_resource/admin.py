from __future__ import unicode_literals
from django.contrib import admin

from .models import *

admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Result)
admin.site.register(Level)
admin.site.register(Class)
admin.site.register(UserType)
admin.site.register(Subject)
