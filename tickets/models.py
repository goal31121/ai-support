from django.db import models #models is Django’s module to create database tables.
from django.contrib.auth.models import User #User is the default Django user model, used here to link tickets to customers and responders.


#This defines a table called Ticket in your database.
#Each instance of this class is a row in the tickets_ticket table.
class Ticket(models.Model):
    CATEGORY_CHOICES = [
        ('Billing', 'Billing'),
        ('Technical', 'Technical'),
        ('General', 'General'),
    ]
#These are fixed options for category and status fields.
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Replied', 'Replied'),
    ]
    
    #Customer side
    #Links ticket to the user who created it. If the user is deleted, all their tickets are also deleted (CASCADE).
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    #Short title of the ticket
    subject = models.CharField(max_length=255)
    
    message = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    

    # Admin side
    response = models.TextField(blank=True, null=True)
    responder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='responses')
    ai_generated = models.BooleanField(default=False)
    ai_classified = models.BooleanField(default=False)  # new field

#When you print a Ticket object, it shows its subject instead of a database ID
    def __str__(self):
        return self.subject
