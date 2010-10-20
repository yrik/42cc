from django.db import models
import datetime
from django.db.models.signals import post_save, post_delete
from django.core.signals import request_started
from core.forms import PersonForm


class Http(models.Model):
    """
    #Http item
    # New item
    >>> i = Http(path="path", user="user")
    >>> i.path
    'path'
    >>> i.user
    'user'
    """
    path = models.TextField(null=True, blank=True)
    method = models.TextField(null=True, blank=True)
    user = models.TextField(null=True, blank=True)
    POST = models.TextField(null=True, blank=True)
    GET = models.TextField(null=True, blank=True)
    META = models.TextField(null=True, blank=True)
    

    def get_fields(self):
        return [(field.name, field.value_to_string(self))\
        for field in self._meta.fields]


    def  __unicode__(self):
        s = ''
        for field in self._meta.fields:
            s += "%s:%s;" % (field.name, field.value_to_string(self)[:50])
        return s

class Log(models.Model):
    """
    #Log item
    # New item
    >>> i = Log(content="content")
    >>> i.content
    'content'
    """
    PC = (
        (0, 'low'),
        (1, 'normal'),
        (2, 'high'),
    )
    content = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True, auto_now=True)
    priority = models.IntegerField(choices=PC, default=0)

    def __unicode__(self):
        return '%d %s in %s' % (self.priority, self.content, self.date)


class Person(models.Model):
    """
    Person with properties
    # New person
    >>> p = Person(name="name", surname="surname",\
                    bio="bio",contacts="phone:123456789")
    >>> p.name
    'name'
    >>> p.surname
    'surname'
    >>> p.bio
    'bio'
    >>> p.contacts
    'phone:123456789'
    """
    name = models.CharField(null=True, max_length=250)
    surname = models.CharField(null=True, max_length=250)
    bio = models.TextField(null=True, max_length=250)
    contacts = models.TextField(null=True, max_length=250)
    birth_date = models.DateField(null=True, blank=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self))\
        for field in self._meta.fields]

    def __unicode__(self):
        return self.name + ' ' + self.surname


def delete_callback(sender, instance, signal, *args, **kwargs):
    l = Log(content="object '%s' is deleted" % instance)
    l.save()


def save_callback(sender, instance, signal, *args, **kwargs):
    if sender != Log:
        if kwargs.get('created', True):
            l = Log(content="object '%s' is created" % instance)
        else:
            l = Log(content="object '%s' is edited" % instance)
        l.save()


post_save.connect(save_callback)
post_delete.connect(delete_callback)
