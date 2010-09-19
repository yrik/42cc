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

    p = Person.objects.filter(name="Iurii", surname="Kriachko")
    return render_to_response('index.html',{'items':p})

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

    return render_to_response('index.html', {
        'form': form,
        'items':items,
    },
     context_instance=RequestContext(request),
    )


