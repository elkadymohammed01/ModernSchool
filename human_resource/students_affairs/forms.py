from django import forms
from ..models import *


class AddStudent(forms.Form):
    levels = [(item.id, item.level) for item in Level.objects.all()]
    levels.insert(0, (0, '----'))
    classes = [(item.id, item.class_name) for item in Class.objects.all()]
    classes.insert(0, (0, '----'))

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    age = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(choices=tuple((item.id, item.type)for item in UserType.objects.all()),
                             widget=forms.Select(attrs={'class': 'form-select'}))
    level = forms.ChoiceField(choices=levels,
                              widget=forms.Select(attrs={'class': 'form-select'}))
    class_name = forms.ChoiceField(choices=classes,
                                   widget=forms.Select(attrs={'class': 'form-select'}))
