from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass 
    
    def __str__(self):
        return self.username #abstract user automatically has a username and we are inheriting from that
        
    


