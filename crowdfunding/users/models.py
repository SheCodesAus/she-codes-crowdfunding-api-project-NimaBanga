from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser): #abstractuser has default field but we can add the ones below
    bio = models.TextField()
    photo = models.URLField() # in this case user will have to give a URL to their photo while saving it themselves on cloud Can change it to 'Filefield' but will have to designate a folder within project to save a photo upload by user
    address = models.TextField() #in react I can validate teh address with google database
    
    def __str__(self):
        return self.username #abstract user automatically has a username and we are inheriting from that
        
    


