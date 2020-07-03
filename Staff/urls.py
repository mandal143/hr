from django.urls import path
from . import views


app_name = 'Staff'

urlpatterns = [
    # ATTENDANCE 
    path('attendance_dashboard/^(?P<id>\w+)/$', views.attendance_dashboard, name='attendance_dashboard'),
    # path('attendance_edit/^(?P<login_id>\w+)/$', views.attendance_edit, name='attendance_edit'),
    # path('attendance_edit_save/^(?P<login_id>\w+)/$', views.attendance_edit_save, name='attendance_edit_save'),
    path('home_page/^(?P<id>\w+)/$', views.home_page, name='home_page'),
	
	# DPR
	path('dpr_dashboard/^(?P<id>\w+)/$', views.dpr_dashboard, name='dpr_dashboard'),
	path('dpr_form/^(?P<id>\w+)/$', views.dpr_form, name='dpr_form'),
	path('dpr_form_save/^(?P<id>\w+)/$', views.dpr_form_save, name='dpr_form_save'),
	path('dpr_status_form/^(?P<enquiry_id>\w+)/^(?P<id>\w+)/$', views.dpr_status_form, name='dpr_status_form'),
	path('dpr_status_form_save/^(?P<enquiry_id>\w+)/^(?P<id>\w+)/$', views.dpr_status_form_save, name='dpr_status_form_save'),
	# path('export_users_csv/$', views.export_users_csv, name='export_users_csv'),
	
	# HOLIDAY
	path('holiday_dashboard/^(?P<id>\w+)/$', views.holiday_dashboard, name='holiday_dashboard'),
	# path('add_holiday/^(?P<id>\w+)/$', views.add_holiday, name='add_holiday'),
	# path('add_holiday_save/^(?P<id>\w+)/$', views.add_holiday_save, name='add_holiday_save'),
	# path('holiday_edit/^(?P<holiday_id>\w+)/^(?P<id>\w+)/$', views.holiday_edit, name='holiday_edit'),
	# path('holiday_edit_save/^(?P<holiday_id>\w+)/^(?P<id>\w+)/$', views.holiday_edit_save, name='holiday_edit_save'),
	
	# NOTICE 
	path('notice_dashboard/^(?P<id>\w+)/$', views.notice_dashboard, name='notice_dashboard'),	
	# path('add_notice/^(?P<id>\w+)/$', views.add_notice, name='add_notice'),
	# path('add_notice_save/^(?P<id>\w+)/$', views.add_notice_save, name='add_notice_save'),
	# path('notice_edit/^(?P<notice_id>\w+)/^(?P<id>\w+)/$', views.notice_edit, name='notice_edit'),
	# path('notice_edit_save/^(?P<notice_id>\w+)/^(?P<id>\w+)/$', views.notice_edit_save, name='notice_edit_save'),
	
	
	# GRIEVANCE
	path('grievance_dashboard/^(?P<id>\w+)/$', views.grievance_dashboard, name='grievance_dashboard'),	
	path('grievance_add/^(?P<id>\w+)/$', views.grievance_add, name='grievance_add'),	
	path('grievance_add_save/^(?P<id>\w+)/$', views.grievance_add_save, name='grievance_add_save'),	
	
	
	# LEAVE
	path('leave_dashboard/^(?P<id>\w+)/$', views.leave_dashboard, name='leave_dashboard'),	
	path('leave_apply/^(?P<id>\w+)/$', views.leave_apply, name='leave_apply'),	
	path('leave_apply_save/^(?P<id>\w+)/$', views.leave_apply_save, name='leave_apply_save'),	
	# path('leave_accept/^(?P<id>\w+)/$', views.leave_accept, name='leave_accept'),	
	# path('leave_reject/^(?P<id>\w+)/$', views.leave_reject, name='leave_reject'),	
	
	#PAYROLL
	path('payroll_dashboard/^(?P<id>\w+)/$', views.payroll_dashboard, name='payroll_dashboard'),	
	# path('add_payroll/^(?P<id>\w+)/$', views.add_payroll, name='add_payroll'),
	# path('add_payroll_save/^(?P<id>\w+)/$', views.add_payroll_save, name='add_payroll_save'),
	# path('payroll_edit/^(?P<payroll_id>\w+)/^(?P<id>\w+)/$', views.payroll_edit, name='payroll_edit'),
	# path('payroll_edit_save/^(?P<payroll_id>\w+)/^(?P<id>\w+)/$', views.payroll_edit_save, name='payroll_edit_save'),
	
	#USER
	# path('user_dashboard/^(?P<id>\w+)/$', views.user_dashboard, name='user_dashboard'),
	# path('add_new_user/^(?P<id>\w+)/$', views.add_new_user, name='add_new_user'),
	# path('user_deactivate/^(?P<user_id>\w+)/^(?P<id>\w+)/$', views.user_deactivate, name='user_deactivate'),
	# path('user_activate/^(?P<user_id>\w+)/^(?P<id>\w+)/$', views.user_activate, name='user_activate'),
	# path('signup/^(?P<id>\w+)/$', views.signup, name='signup'),
	
	
]