from django.contrib import admin

# Register your models here.
from .models import Enquiries, Holidays, Notices, Grievances, Leaves, Payrolls

# admin.site.register(Enquiries)
@admin.register(Enquiries)
class EnquiriesAdmin(admin.ModelAdmin):
    list_display = ['emp_code','dpr_no','dpr_month','pros_name']
    list_filter = ['emp_code']
	
	
@admin.register(Holidays)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ['holiday_no','holiday_date','holiday_day','holiday_reason','holiday_city']
    list_filter = ['holiday_no']
	
@admin.register(Notices)
class NoticesAdmin(admin.ModelAdmin):
    list_display = ['notice_no','notice_date','notice_details']
    list_filter = ['notice_no']
	
@admin.register(Grievances)
class GrievancesAdmin(admin.ModelAdmin):
    list_display = ['user','grievance_dated','grievance_details']
    list_filter = ['user']
	

@admin.register(Payrolls)
class PayrollsAdmin(admin.ModelAdmin):
    list_display = ['user','pay_month','net_salary','status']
    list_filter = ['user']
	
	
@admin.register(Leaves)
class LeavesAdmin(admin.ModelAdmin):
    list_display = ['user','leave_no_of_days','leave_from_date','leave_to_date']
    list_filter = ['user']