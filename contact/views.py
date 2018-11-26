from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm
from .utils import send_to_pubsub


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = '/success/'   

    def form_valid(self, form):
        send_to_pubsub(form.cleaned_data)
        return super().form_valid(form)
