from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from polls.models import LoginLogoutLog
from Administration.models import Enquiries, Holidays, Notices, Grievances, Leaves, Payrolls, SignUpForm
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django.utils.timezone import localtime, get_current_timezone
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date
import pprint
import csv
import pytz
app = "Staff"



# ATTENDANCE DASHBOARD

def attendance_dashboard(request,id):
    user = User.objects.get(id=id)
    pprint.pprint(user)
    user_details = LoginLogoutLog.objects.filter(user=user)
    pprint.pprint(user_details)
    if not user.is_superuser:       
        pprint.pprint(user)
        return render(request,  app+'/attendance_dashboard.html', {'user_details':user_details, 'user':user})
    else:
	    return render(request,  'polls/login.html', {'error_message': 'Error: You Dont Have the Permission..!!'})  
		
def home_page(request,id):
    user = User.objects.get(id=id)
    pprint.pprint(user.username)
    user_details = LoginLogoutLog.objects.all()
    return render(request,   'polls/staff.html', {'user_details':user_details, 'user':user})	


#DPR DASHBOARD

def dpr_dashboard(request,id):
    user = User.objects.get(id=id)
    enquiry = Enquiries.objects.filter(emp_code=user)
    # enquiry = Enquiries.objects.all()
    return render(request, app + '/dpr_dashboard.html', { 'enquiries_list': enquiry, 'user':user })	

def dpr_form(request,id):
    user = User.objects.get(id=id)
    return  render(request, app+'/dpr_form.html', {'user': user})

def dpr_form_save(request,id):
    user = User.objects.get(id=id) 
    id = user.id
    if request.method == 'POST':
	    emp_code = request.POST['Emp_Code']
	    dpr_no = request.POST['DPR_Number']
	    dpr_month = request.POST['DPR_Month']
	    pros_name = request.POST['Prospective_Name']
	    pros_date = request.POST['DOB_Date']
	    pros_month = request.POST['DOB_Month']
	    pros_year = request.POST['DOB_Year']
	    enquiry_by = request.POST['Enquiry_By']
	    relation = request.POST['Relationship']
	    phone1 = request.POST['Phone1']
	    phone2 = request.POST['Phone2']
	    pros_state = request.POST['Prospective_Domicile_State']
	    pros_city = request.POST['Prospective_City']
	    pros_course = request.POST['Interested_Course']
	    pros_other = request.POST['Interested_Course_Others']
	    pros_interest_states_1 = request.POST['Interested_State1']
	    pros_interest_states_2 = request.POST['Interested_State2']
	    pros_interest_states_3 = request.POST['Interested_State3']
	    pros_10_marks = request.POST['Percentage_10']
	    pros_12_marks = request.POST['Percentage_12']
	    pros_subject_1 = request.POST['Core_Subject1']
	    pros_subject_2 = request.POST['Core_Subject2']
	    pros_subject_3 = request.POST['Core_Subject3']
	    pros_entrance_exam1 = request.POST['Enterance_Exam1']
	    pros_entrance_exam2 = request.POST['Enterance_Exam2']
	    pros_entrance_exam3 = request.POST['Enterance_Exam3']
	    pros_entrance_exam4 = request.POST['Enterance_Exam4']
	    pros_budget = request.POST['Prospective_Budget']
	    pros_register_date = request.POST['Reg_by_Date']
	    pros_register_month = request.POST['Reg_By_Month']
	    pros_register_year = request.POST['Reg_By_Year']
	    pros_register_remarks = request.POST['Remarks']
	    enquiry = Enquiries.objects.create(emp_code=emp_code, dpr_no=dpr_no, dpr_month=dpr_month, pros_name=pros_name, pros_date=pros_date,
            		pros_month=pros_month, pros_year=pros_year, enquiry_by=enquiry_by, relation=relation, phone1=phone1, phone2=phone2,
					pros_state=pros_state, pros_city=pros_city, pros_course=pros_course, pros_other=pros_other, pros_interest_states_1=pros_interest_states_1,
                    pros_interest_states_2=pros_interest_states_2, pros_interest_states_3=pros_interest_states_3, pros_10_marks=pros_10_marks,
                    pros_12_marks=pros_12_marks, pros_subject_1=pros_subject_1, pros_subject_2=pros_subject_2, pros_subject_3=pros_subject_3,
                    pros_entrance_exam1=pros_entrance_exam1, pros_entrance_exam2=pros_entrance_exam2, pros_entrance_exam3=pros_entrance_exam3,
                    pros_entrance_exam4=pros_entrance_exam4, pros_budget=pros_budget, pros_register_date=pros_register_date,pros_register_month=pros_register_month,
					pros_register_year=pros_register_year,pros_register_remarks=pros_register_remarks)
	    pprint.pprint("hiii")
		# subject="DPR ENQUIRY"
		# message=(' Emp Code:'+str(emp_code)+'\n Dpr No:'+str(dpr_no)+'\n Dpr Month:'+str(dpr_month)+'\n Prospective Name:'+str(pros_name)+'\n DOB:'+str(pros_date)+'/'+str(pros_month)+'/'+str(pros_year)+
		         # '\n Enquiry By:'+str(enquiry_by)+'\n Relationship:'+str(relation)+'\n Phone 1:'+str(phone1)+'\n Phone 2:'+str(phone2)+'\n Prospective State:'+str(pros_state)+
		         # '\n Prospective City:'+str(pros_city)+'\n Prospective Course:'+str(pros_course) +'\n Other:'+str(pros_other)+'\n State1:'+str(pros_interest_states_1)+
		         # '\n State2:'+str(pros_interest_states_2)+'\n State3:'+str(pros_interest_states_3)+'\n 10th Marks:'+str(pros_10_marks)+'\n 12th Marks:'+str(pros_12_marks)+'\n Core Subject1:'+str(pros_subject_1)+'\n Core Subject2:'+str(pros_subject_2)+
		         # '\n Core Subject3:'+str(pros_subject_3)+'\n Enterance Exam 1:'+str(pros_entrance_exam1)+'\n Enterance Exam 2:'+str(pros_entrance_exam2)+'\n Enterance Exam 3:'+str(pros_entrance_exam3)+
		         # '\n Enterance Exam 4:'+str(pros_entrance_exam4)+'\n Prospective Budget:'+str(pros_budget)+'\n Register DD MM YY:'+str(pros_register_date)+'/'+str(pros_register_month)+'/'+str(pros_register_year)+
		         # '\n Remarks:'+str(pros_register_remarks))
		# email_from = settings.EMAIL_HOST_USER
		# recipient_list = ['chanakya.factor@gmail.com', 'animesh472@gmail.com']
		# send_mail(subject,message,email_from,recipient_list)
	    return HttpResponseRedirect(reverse(app+':dpr_dashboard',args=(str(id),)))
		
		
#HOLIDAY DASHBOARD

def holiday_dashboard(request,id):
    user =  User.objects.get(id=id)
    holiday = Holidays.objects.all()
    return render(request, app + '/holiday_dashboard.html', {'holidays_lists': holiday, 'user': user  })
	
# NOTICE BOARD

def notice_dashboard(request,id):
    user =  User.objects.get(id=id)
    notice = Notices.objects.all()
    return render(request, app + '/notice_dashboard.html', {'notice_lists': notice, 'user': user  })	
	
	
# LEAVE
	
def leave_dashboard(request,id):
    user =  User.objects.get(id=id)
    leave = Leaves.objects.filter(user=user)
    return render(request, app + '/leave_dashboard.html', {'leave_lists': leave, 'user': user  })
	
def leave_apply(request,id):
    user= User.objects.get(id=id)	
    return render(request, app + '/leave_apply.html', { 'user': user  })
	
def leave_apply_save(request,id):
    user = User.objects.get(id=id)
    id = user.id
    if request.method == 'POST':
	    leave_no_of_days = request.POST['leave_no_of_days']
	    leave_from_date = request.POST['leave_from_date']
	    pprint.pprint(leave_from_date)
	    leave_to_date = request.POST['leave_to_date']
	    pprint.pprint(leave_to_date)
	    leave_reason = request.POST['leave_reason']
	    pprint.pprint(leave_reason)
	    leaves=Leaves.objects.create(user=user, leave_no_of_days=leave_no_of_days, leave_from_date=leave_from_date, leave_to_date=leave_to_date, leave_reason=leave_reason)
	    pprint.pprint(leaves)
	    return HttpResponseRedirect(reverse(app+':leave_dashboard',args=(str(id),)))
		
#GRIEVANCE

def grievance_dashboard(request,id):
    user =  User.objects.get(id=id)
    grievance = Grievances.objects.filter(user=user)
    return render(request, app + '/grievance_dashboard.html', {'grievance_lists': grievance, 'user': user  })

def grievance_add(request,id):
    user =  User.objects.get(id=id)
    return render(request, app + '/grievance_add.html', { 'user': user })
	
	
def grievance_add_save(request,id):
    user = User.objects.get(id=id)
    id = user.id
    if request.method == 'POST':
	    grievance_details = request.POST['grievance_details']
	    grievance=Grievances.objects.create(user=user, grievance_details=grievance_details)
	    return HttpResponseRedirect(reverse(app+':grievance_dashboard',args=(str(id),)))
		
#PAYROLL

def payroll_dashboard(request,id):
    user =  User.objects.get(id=id)
    payroll = Payrolls.objects.filter(user=user)
    return render(request, app + '/Payroll_dashboard.html', {'payroll_lists': payroll, 'user': user  })
	
	
