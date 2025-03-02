from django.apps import AppConfig

#Tells Django about the configuration of the tickets app
class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Specifies the default type for primary keys in models.
    name = 'tickets' #used to locate app
    
    
    
#This file lets Django know how to set up and manage the tickets app automatically.