from django.shortcuts import render_to_response
from core.models import Person

"""
>>> from django.test import Client
>>> from django.core.urlresolver import reverse

>>> response = client.get(reverse(''))
>>> response.status_code
200
"""

def index(request):
    """
    try:
        p = Person.objects.get(name="Iurii", surname="Kriachko")
    except Person.DoesNotExist:
        p= Person(name="Iurii",surname="Kriachko",bio="my bio", contacts="phone:093 762 5 172")
        p.save()
    """
    p = Person.objects.get(name="Iurii", surname="Kriachko")
    return render_to_response('index.html',{'p':p})
