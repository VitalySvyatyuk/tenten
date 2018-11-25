from django.shortcuts import render
from django.views.generic import FormView

from .forms import ContactForm

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'       

    def form_valid(self, form):
        import pdb; pdb.set_trace()
        print(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        import pdb; pdb.set_trace()
        print(form.errors)
        return super().form_invalid(form)
