from django.contrib import admin

# Register your models here.
from .models import TeamLeaders, TeamMembers


@admin.register(TeamLeaders)
class TeamLeadersAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_filter = ['user']
	
@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['leader']
    list_filter = ['leader']