from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    title=models.CharField(max_length=200) #used for shorter texts versus TextField
    description=models.TextField()
    goal=models.IntegerField()
    image=models.URLField() #Helps to point to a source stored somewhere else
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True) #auto now add enable adding time of creation of project automatically
    owner=models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='owner_projects'
    ) #On_delete cascade means if user deleted then their projects deleted as well.
    project_date = models.DateField() #NB
    project_starttime = models.DateTimeField() #NB
    project_endtime = models.DateTimeField() #NB

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField() #Do I delete it???
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='pledges')
    supporter = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    # pledge_date = models.DateTimeField(auto_now_add=True)

    
