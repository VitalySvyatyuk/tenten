from django.urls import path
from django.views.generic import TemplateView
from .views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', TemplateView.as_view(template_name="contact/success.html"))
]