#forms.py
from django import forms
from core.widgets import DateTimeWidget
import datetime


class PersonForm(forms.Form):
        id = forms.CharField()
        birth_date = forms.DateField(initial=datetime.date.today, \
                    required=False, widget=DateTimeWidget)
        name = forms.CharField()
        surname = forms.CharField(required=False)
        bio = forms.CharField(required=False, widget=forms.Textarea)
        contacts = forms.CharField(required=False, widget=forms.Textarea)

        class Media:
            js = (
                '/static/js/jquery-1.4.2.min.js',
                '/static/js/jquery.form.js',
                '/static/js/custom.js',
            )
