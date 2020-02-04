from django.contrib import admin

# Register your models here.
from .models import LoginLogoutLog

@admin.register(LoginLogoutLog)
class LoginLogoutLogAdmin(admin.ModelAdmin):
    list_display = ['user','login_time','logout_time','remarks']
    list_filter = ['user']
    
