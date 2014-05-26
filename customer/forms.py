from customer.models import Customer, Meeting
from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        ordering = ['name']
        birth_date = forms.DateField(widget=widgets.AdminDateWidget(format='%d/%m/%Y'), input_formats=('%d/%m/%Y',))
        exclude = ['meeting']

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        exclude = ['customer']

class SearchForm(forms.Form):
    search_word = forms.CharField()

    def clean_search_word(self):
       word = self.cleaned_data['search_word']
       return word


