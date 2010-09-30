from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Person, PersonForm
from django.http import HttpResponseRedirect
def index(request):

    """
    >>> from django.test import Client
    >>> from django.core.urlresolver import reverse
    >>> client = Client()

    >>> response = client.get('')
    >>> response.status_code
    200
    """

    p = Person.objects.filter(id=1,name="Iurii", surname="Kriachko")
    return render_to_response('index.html',{'items':p})

def settings(request):

    """
    >>> from django.test import Client
    >>> from django.core.urlresolver import reverse
    >>> client = Client()

    >>> response = client.get('/settings')
    >>> response.status_code
    200
    """

    return render_to_response('context.html', context_instance=RequestContext(request))




def add_person(request):

    """
    >>> from django.test import Client
    >>> from django.core.urlresolver import reverse
    >>> client = Client()

    >>> response = client.get('add_person')
    >>> response.status_code
    200

    >>> client.post('/add_person/', {'name': 'fred')
    200
    """


    items = Person.objects.all()
    
    if request.method == 'POST': # If the form has been submitted...
        form = PersonForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            newPerson = Person(name=form.cleaned_data['name'],bio=form.cleaned_data['bio'],contacts=form.cleaned_data['contacts'],surname=form.cleaned_data['surname'])
            newPerson.save()

            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = PersonForm() # An unbound form

    return render_to_response('add_person.html', {
        'form': form,
        'items':items,
    },
     context_instance=RequestContext(request),
    )


def edit_person(request):

    """
    >>> from django.test import Client
    >>> from django.core.urlresolver import reverse
    >>> client = Client()

    >>> response = client.get('edit_person')
    >>> response.status_code
    200

    >>> client.post('/edit_person/', {'name': 'fred')
    200
    """


    items = Person.objects.all()
    
    if request.method == 'POST': # If the form has been submitted...
        form = PersonForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            p = Person.objects.get(id=form.cleaned_data['id'])
            p.name=form.cleaned_data['name']
            p.bio=form.cleaned_data['bio']
            p.contacts=form.cleaned_data['contacts']
            p.surname=form.cleaned_data['surname']
            p.save()

            return HttpResponseRedirect('/') # Redirect after POST
    else:
        p = Person.objects.get(name="Iurii", surname="Kriachko",id=1)
        form = PersonForm({'id':p.id,'name':p.name,'surname':p.surname,'bio':p.bio,'contacts':p.contacts})

    return render_to_response('edit_person.html', {
        'form': form,
        'items':items,
    },
     context_instance=RequestContext(request),
    )


