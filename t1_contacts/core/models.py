from django.db import models
import datetime
from django.db.models.signals import post_save, post_delete
from django.core.signals import request_started
from core.forms import PersonForm


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
    priority = models.IntegerField(choices=PC, default=0)

    def __unicode__(self):
        return '%d %s' % (self.priority, self.content)


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
        for field in Person._meta.fields]

    def __unicode__(self):
        return self.name + ' ' + self.surname


def delete_callback(sender, instance, signal, *args, **kwargs):
    l = Log(content="object '%s' is deleted" % instance)
    Log.save(l)


def save_callback(sender, instance, signal, *args, **kwargs):
    if sender != Log:
        if kwargs.get('created', True):
            l = Log(content="object '%s' is created" % instance)
        else:
            l = Log(content="object '%s' is edited" % instance)
        Log.save(l)


post_save.connect(save_callback)
post_delete.connect(delete_callback)
