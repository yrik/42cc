from django.shortcuts import render_to_response
from django.template import RequestContext
from core.models import Person, PersonForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import simplejson

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

def first10items(request):

    """
    >>> from django.test import Client
    >>> response = client.get('/first10items')
    >>> response.status_code
    200
    """

    p = Person.objects.all()[:5]
    return render_to_response('first10items.html',{'items':p})


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
            newPerson = Person(name=form.cleaned_data['name'],bio=form.cleaned_data['bio'],
                        contacts=form.cleaned_data['contacts'],surname=form.cleaned_data['surname'],birth_date=form.cleaned_data['birth_date'])
            newPerson.save()
    
        if request.is_ajax():
            rdict = {'bad':'false'}
            if not form.is_valid():
                rdict.update({'bad':'true'})
                d={}
                for e in form.errors.iteritems():
                    d.update({e[0]:unicode(e[1])})
                rdict.update({'errs': d  })
            json = simplejson.dumps(rdict, ensure_ascii=False)
            return HttpResponse( json, mimetype='application/javascript')
        else:
            return HttpResponseRedirect('/') # Redirect after POST
   
    else:
        form = PersonForm() # An unbound form

    return render_to_response('add_person.html', {
        'form': form,
        'items':items,
    },
     context_instance=RequestContext(request),
    )

@login_required
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
            p.birth_date=form.cleaned_data['birth_date']
            p.save()
        
        if request.is_ajax():
            rdict = {'bad':'false'}
            if not form.is_valid():
                rdict.update({'bad':'true'})
                d={}
                for e in form.errors.iteritems():
                    d.update({e[0]:unicode(e[1])})
                rdict.update({'errs': d  })
            json = simplejson.dumps(rdict, ensure_ascii=False)
            return HttpResponse( json, mimetype='application/javascript')
        else:
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        try:
            p = Person.objects.get(name="Iurii", surname="Kriachko",id=1)
            form = PersonForm({'id':p.id,'name':p.name,'surname':p.surname,'bio':p.bio,'contacts':p.contacts,'birth_date':p.birth_date})
        except:
            return HttpResponseRedirect('/')

    return render_to_response('edit_person.html', {
        'form': form,
        'items':items,
    },
     context_instance=RequestContext(request),
    )


