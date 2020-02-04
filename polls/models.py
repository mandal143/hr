from django.db import models
from django.contrib.auth.models import User
import datetime


class LoginLogoutLog(models.Model):
    login_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # session_key = models.CharField(max_length=100, blank=False, null=False)
    # host = models.CharField(max_length=100, blank=False, null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    # logout_time = models.TimeField(blank=True, null=True, default=datetime.time(18, 30))
	
    def __str__(self):
	    return str(self.login_id)

