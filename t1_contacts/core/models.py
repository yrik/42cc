from django.db import models
from django import forms
from core.widgets import DateTimeWidget
import datetime

class Person(models.Model):
    """
    Person with properties
    # New person
    >>> p = Person(name="name",surname="surname",bio="bio",contacts="phone:123456789")
    >>> p.name
    'name'
    >>> p.surname
    'surname'
    >>> p.bio
    'bio'
    >>> p.contacts
    'phone:123456789'
    """
    name = models.CharField(null=True,max_length=250)
    surname = models.CharField(null=True ,max_length=250)
    bio = models.TextField(null=True ,max_length=250)
    contacts = models.TextField(null=True ,max_length=250)
    birth_date = models.DateField(null=True, blank=True )

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Person._meta.fields]


class PersonForm(forms.Form):
        id = forms.CharField()
        birth_date = forms.DateField(initial=datetime.date.today,required=False, widget=DateTimeWidget)
        contacts = forms.CharField(required=False,widget=forms.Textarea)
        bio = forms.CharField(required=False,widget=forms.Textarea)
        surname = forms.CharField(required=False)
        name = forms.CharField()
