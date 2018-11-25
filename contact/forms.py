from django.forms import Form, CharField, EmailField, Textarea, RegexField

class ContactForm(Form):
    first_name = CharField(required=True, min_length=2, max_length=50)
    last_name = CharField(required=True, min_length=2, max_length=50)
    email = EmailField(required=True, min_length=2, max_length=50)
    phone_number = RegexField(regex=r'^\+?1?\d{9,15}$', 
        error_messages={'invalid': 'Phone number must be entered in the format: "+971559999999"'})
    subject = CharField(required=True, min_length=2, max_length=255)
    message = CharField(widget=Textarea)
