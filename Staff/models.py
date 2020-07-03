from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TeamLeaders(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, unique=True)
	
    def __str__(self):
	    return str(self.user)
		
class TeamMembers(models.Model):
    
    id = models.AutoField(primary_key=True)
    leader = models.ForeignKey(TeamLeaders, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    user = models.ManyToManyField(User)
	
    def __str__(self):
	    return str(self.leader)
		