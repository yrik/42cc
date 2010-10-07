from django.db import models
from django import forms
from core.widgets import DateTimeWidget
import datetime
from django.db.models.signals import post_save, post_delete
from django.core.signals import request_started


class RequestLog(models.Model):
    """
    RequestLog item
    # New item
    >>> i = Log(content="content")
    >>> i.content
    'content'
    """
    PC = (
        (0,'low'),
        (1,'normal'),
        (2,'high'),
    )
    content = models.TextField(null=True,blank=True )
    priority = models.IntegerField(choices=PC, default=0)

    def __unicode__(self):
        return '%d %s' % (self.priority, self.content)
 
class Log(models.Model):
    """
    Log item
    # New item
    >>> i = Log(content="content")
    >>> i.content
    'content'
    """
    content = models.TextField(null=True,blank=True )
    
    def __unicode__(self):
        return self.content
 
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
    
    def __unicode__(self):
        return self.name+' '+self.surname

class PersonForm(forms.Form):
        id = forms.CharField()
        birth_date = forms.DateField(initial=datetime.date.today,required=False, widget=DateTimeWidget)
        name = forms.CharField()
        surname = forms.CharField(required=False)
        bio = forms.CharField(required=False,widget=forms.Textarea)
        contacts = forms.CharField(required=False,widget=forms.Textarea)
        
        class Media:
            js = (
                '/static/js/jquery-1.4.2.min.js',
                '/static/js/jquery.form.js',
                '/static/js/custom.js',
            )



def request_callback(sender, *args, **kwargs):
    content =''
    r = RequestLog(content=sender)
    r.save()

def delete_callback(sender, instance, signal, *args, **kwargs):
    l=Log(content="object '%s' is deleted" % instance)
    Log.save(l)
         
def save_callback(sender, instance, signal, *args, **kwargs):
    if sender != Log :
        if kwargs.get('created', True):
            l=Log(content="object '%s' is created" % instance)
        else:
            l=Log(content="object '%s' is edited" % instance)
        Log.save(l)
         
post_save.connect(save_callback)
post_delete.connect(delete_callback)
request_started.connect(request_callback)
