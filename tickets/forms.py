from django import forms
from .models import Ticket

#Provides a form for customers to create a new support ticket
#Inherits from forms.ModelForm, which automatically creates a form based on a model
#The Meta class specifies which model to use (Ticket) and which fields should be included in the form
#This form is used in the create_ticket view to take user input and save it as a new Ticket object in the database

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message']
