from django.db import models
from django import forms
from core.widgets import DateTimeWidget

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
    birth_date = models.TextField(null=True, max_length=200)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Person._meta.fields]


class PersonForm(forms.Form):
        name = forms.CharField()
        surname = forms.CharField(required=False)
        bio = forms.CharField(required=False,widget=forms.Textarea)
        contacts = forms.CharField(required=False,widget=forms.Textarea)
        birth_date = forms.CharField(required=False, widget=DateTimeWidget)
        id = forms.CharField()
