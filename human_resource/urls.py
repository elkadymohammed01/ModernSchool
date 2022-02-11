from django.conf.urls import url
from .students_affairs.views import students_home

urlpatterns = [
    url('student/', students_home)
]