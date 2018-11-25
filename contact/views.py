from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/success/'    

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)
