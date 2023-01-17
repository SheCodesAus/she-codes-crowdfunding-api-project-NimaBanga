from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200) #used for shorter texts versus TextField
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField() #Helps to point to a source stored somewhere else
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True) #auto now add enable adding time of creation of project automatically
    owner=models.CharField(max_length=200) #will need to change this from charfield to foreign key so it can reference id of the users once created
    

    
