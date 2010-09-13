from django.db import models

class Person(models.Model):
    """
    Person with properties
    # New person
    >>> p = Person(name="name",surname="surneme",bio="bio",contacts="phone:123456789")
    >>> p.name
    'name'
    >>> p.surname
    'surname'
    >>> p.bio
    'bio'
    >>> p.contacts
    'phone:123456789'
    """
