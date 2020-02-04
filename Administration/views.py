from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from polls.models import LoginLogoutLog
from .models import Enquiries, Holidays, Notices, Grievances, Leaves, Payrolls, SignUpForm
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django.utils.timezone import localtime, get_current_timezone
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
import pprint
import csv
import pytz
app = "Administration"



# ATTENDANCE DASHBOARD

def attendance_dashboard(request,id):
    user = User.objects.get(id=id)
    if user.is_superuser:       
        pprint.pprint(user)
        user_details = LoginLogoutLog.objects.all()
        return render(request,  app+'/attendance_dashboard.html', {'user_details':user_details, 'user':user})
    else:
	    return render(request,  'polls/login.html', {'error_message': 'Error: You Dont Have the Permission..!!'})  
	    
	
	
	
def attendance_edit(request,login_id,id):
    user = User.objects.get(id=id)
    pprint.pprint(login_id)
    # id_get = str(id.login_id)
    details = LoginLogoutLog.objects.get(login_id=login_id)
    pprint.pprint(details)
    return render(request,  app+'/attendance_edit.html', {'details':details,'user':user})
	
	
def attendance_edit_save(request,login_id,id):

    user = User.objects.get(id=id)
    id = user.id
    pprint.pprint(user.id)
    pprint.pprint(login_id)
    pprint.pprint(login_id)
    remarks = request.POST['remarks']
    user_details = LoginLogoutLog.objects.get(login_id=login_id)
    user_details.remarks = remarks
    user_details.save()
    pprint.pprint(user_details)
	
    return HttpResponseRedirect(reverse(app + ':attendance_dashboard',args=(str(id),)))

def home_page(request,id):
    user = User.objects.get(id=id)
    pprint.pprint(user.username)
    user_details = LoginLogoutLog.objects.all()
    return render(request,  'polls/admin.html', {'user_details':user_details, 'user':user})
	
	
#DPR DASHBOARD

def dpr_dashboard(request,id):
    user = User.objects.get(id=id)
    enquiry = Enquiries.objects.all()
    return render(request, app + '/dpr_dashboard.html', {'enquiries_list': enquiry, 'user':user })
	
def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="DPR Reports.csv"'

    writer = csv.writer(response)
    writer.writerow(['Enquiry Date','Emp Code','Dpr No','Dpr Month','Prospective Name',
                  'Phone 1','Domicile','Interested In','State1','State2','State3','12th',
                  'Budget','Reg DD','Reg MM','Reg YY','Remarks'])
	
    users = Enquiries.objects.order_by('enquiry_id').values_list('enquiry_date','emp_code','dpr_no','dpr_month','pros_name',
                  'phone1','pros_state','pros_course','pros_interest_states_1','pros_interest_states_2','pros_interest_states_3','pros_12_marks',
                 'pros_budget','pros_register_date','pros_register_month','pros_register_year','pros_register_remarks')
    for user in users:
        writer.writerow(user)
	
    return response
	
#HOLIDAY DASHBOARD

def holiday_dashboard(request,id):
    user =  User.objects.get(id=id)
    holiday = Holidays.objects.all()
    return render(request, app + '/holiday_dashboard.html', {'holidays_lists': holiday, 'user': user  })
	
def add_holiday(request,id):
    user =  User.objects.get(id=id)
    return render(request, app + '/add_holiday.html', {'user': user})
	
def add_holiday_save(request,id):
    user =  User.objects.get(id=id)
    id = user.id
    if request.method == 'POST':
        holiday_no = request.POST['holiday_no']
        holiday_date = request.POST['holiday_date']
        holiday_day = request.POST['holiday_day']
        holiday_reason = request.POST['holiday_reason']
        holiday = Holidays.objects.create(holiday_no=holiday_no, holiday_date=holiday_date, holiday_day=holiday_day, holiday_reason=holiday_reason)
        return HttpResponseRedirect(reverse(app + ':holiday_dashboard',args=(str(id),)))
    else:
	    pprint.pprint("NOTE: Please Check the Entered Deatils")
	    return render(request, app + '/add_holiday.html')

def holiday_edit(request, holiday_id, id):
    pprint.pprint(id)
    user =  User.objects.get(id=id)
    holiday = Holidays.objects.get(holiday_id=holiday_id)
    pprint.pprint(holiday)
    return render(request, app + '/edit_holiday.html', {'holiday':holiday, 'user': user})
	
def holiday_edit_save(request, holiday_id, id):
    pprint.pprint(holiday_id)
    user =  User.objects.get(id=id)
    id = user.id
    pprint.pprint(id)
    if request.method == 'POST':
        
        pprint.pprint("sfg")
        holiday_no = request.POST['holiday_no']
        holiday_date = request.POST['holiday_date']
        holiday_day = request.POST['holiday_day']
        holiday_reason = request.POST['holiday_reason']
        holiday = Holidays.objects.get(holiday_id=holiday_id)
        holiday.holiday_no = holiday_no
        holiday.holiday_date = holiday_date
        holiday.holiday_day = holiday_day
        holiday.holiday_reason = holiday_reason
        holiday.save()
        pprint.pprint("holiday_edit_save Done")
        return HttpResponseRedirect(reverse(app + ':holiday_dashboard',args=(str(id),)))
    else:
	    pprint.pprint("NOTE: Please Check the Entered Deatils")
	    return render(request, app + '/add_holiday.html')

# NOTICE BOARD

def notice_dashboard(request,id):
    user =  User.objects.get(id=id)
    notice = Notices.objects.all()
    return render(request, app + '/notice_dashboard.html', {'notice_lists': notice, 'user': user  })
	
	
def add_notice(request,id):
    user =  User.objects.get(id=id)
    return render(request, app + '/add_notice.html', {'user':user})
	
def add_notice_save(request,id):
    user =  User.objects.get(id=id)
    id = user.id
    if request.method == 'POST':
        notice_no = request.POST['notice_no']
        notice_details = request.POST['notice_details']
      
        holiday = Notices.objects.create(notice_no=notice_no, notice_details=notice_details)
        return HttpResponseRedirect(reverse(app + ':notice_dashboard',args=(str(id),)))
    else:
	    pprint.pprint("NOTE: Please Check the Entered Deatils")
	    return render(request, app + '/add_notice.html')

def notice_edit(request,notice_id,id):
    user =  User.objects.get(id=id)
    pprint.pprint(id)
    notice = Notices.objects.get(notice_id=notice_id)
    pprint.pprint(notice)
    return render(request, app + '/edit_notice.html', {'notice':notice, 'user':user})
	
def notice_edit_save(request,notice_id,id):
    pprint.pprint(id)
    user =  User.objects.get(id=id)
    id = user.id
    if request.method == 'POST':
        pprint.pprint("sfg")
        notice_no = request.POST['notice_no']
        notice_details = request.POST['notice_details']
     
        notice = Notices.objects.get(notice_id=notice_id)
        notice.notice_no = notice_no
        notice.notice_details = notice_details
        notice.save()
        pprint.pprint("Notice Edit Save Done.")
        return HttpResponseRedirect(reverse(app + ':notice_dashboard',args=(str(id),)))
    else:
	    pprint.pprint("NOTE: Please Check the Entered Deatils")
	    return render(request, app + '/add_notice.html')

	

# LEAVE
	
def leave_dashboard(request,id):
    user =  User.objects.get(id=id)
    leave = Leaves.objects.all()
    return render(request, app + '/leave_dashboard.html', {'leave_lists': leave, 'user': user  })
	
	
def leave_accept(request,leaves_id,id):
    user =  User.objects.get(id=id)
    id = user.id
    leave = Leaves.objects.get(leaves_id=leaves_id)
    leave.leave_status = 'Accepted'
    leave.save()
    return HttpResponseRedirect(reverse(app + ':leave_dashboard',args=(str(id),)))
	
def leave_reject(request,leaves_id,id):
    user =  User.objects.get(id=id)
    id = user.id
    leave = Leaves.objects.get(leaves_id=leaves_id)
    leave.leave_status = 'Rejected'
    leave.save()
    return HttpResponseRedirect(reverse(app + ':leave_dashboard',args=(str(id),)))
	
	
#GRIEVANCE

def grievance_dashboard(request,id):
    user =  User.objects.get(id=id)
    grievance = Grievances.objects.all()
    return render(request, app + '/grievance_dashboard.html', {'grievance_lists': grievance, 'user': user  })
	
#PAYROLL

def payroll_dashboard(request,id):
    user =  User.objects.get(id=id)
    payroll = Payrolls.objects.all()
    return render(request, app + '/Payroll_dashboard.html', {'payroll_lists': payroll, 'user': user  })
	
	
def add_payroll(request,id):
    user =  User.objects.get(id=id)
    user_all = User.objects.all()
    return render(request, app + '/add_payroll.html', {'user':user, 'user_all':user_all})
	
	
def add_payroll_save(request,id):
    usr = User.objects.get(id=id)
    id = usr.id
	
    if request.method == 'POST':
	    
        user_id = request.POST['user']
        pay_month = request.POST['pay_month']
        gross_salary = request.POST['gross_salary']
        no_of_leaves = request.POST['no_of_leaves']
        loss_of_amount = request.POST['loss_of_amount']
        advance_salary = request.POST['advance_salary']
        net_salary = request.POST['net_salary']
        status = request.POST['status']
        user =  User.objects.get(id=user_id)
        Payroll = Payrolls.objects.create(user=user, pay_month=pay_month, gross_salary=gross_salary, 
		           no_of_leaves=no_of_leaves, loss_of_amount=loss_of_amount, advance_salary=advance_salary,
				   net_salary=net_salary, status=status )
        return HttpResponseRedirect(reverse(app + ':payroll_dashboard',args=(str(id),)))
    
    else:
        pprint.pprint("please check the error in the form.")
        return render(request, app + '/add_payroll.html')
		
		
def payroll_edit(request,payroll_id,id):
    user =  User.objects.get(id=id)
    user_all = User.objects.all()
    pprint.pprint(user)
    payroll = Payrolls.objects.get(payroll_id=payroll_id)
    pprint.pprint(payroll)
    return render(request, app + '/edit_payroll.html', {'payroll':payroll, 'user':user, 'user_all':user_all})
	
def payroll_edit_save(request,payroll_id,id):
    user =  User.objects.get(id=id)
    id = user.id
    if request.method == 'POST':
        pprint.pprint("sfg")
        pay_month = request.POST['pay_month']
        gross_salary = request.POST['gross_salary']
        no_of_leaves = request.POST['no_of_leaves']
        loss_of_amount = request.POST['loss_of_amount']
        advance_salary = request.POST['advance_salary']
        net_salary = request.POST['net_salary']
        status = request.POST['status']
     
        payroll = Payrolls.objects.get(payroll_id=payroll_id)
        payroll.pay_month = pay_month
        payroll.gross_salary = gross_salary
        payroll.no_of_leaves = no_of_leaves
        payroll.loss_of_amount = loss_of_amount
        payroll.advance_salary = advance_salary
        payroll.net_salary = net_salary
        payroll.status = status
        payroll.save()
        pprint.pprint("Payroll Edit Save Done.")
        return HttpResponseRedirect(reverse(app + ':payroll_dashboard',args=(str(id),)))
    else:
	    pprint.pprint("NOTE: Please Check the Entered Deatils")
	    return render(request, app + '/edit_payroll.html')	
		
	
#USER	
def user_dashboard(request,id):
    user =  User.objects.get(id=id)
    user_lists = User.objects.filter(is_staff=False)
    return render(request, app + '/user_dashboard.html', {'user_lists': user_lists, 'user': user  })
	
# def add_new_user(request,id):
    # user =  User.objects.get(id=id)
    # form = SignUpForm()
    # return render(request, app + '/signup.html', {'form': form, 'user':user })
	

def user_deactivate(request,user_id,id):
    usr = User.objects.get(id=id)
    id = usr.id
    user =  User.objects.get(id=user_id)
    try:
        user.is_active = False
        user.save()
        pprint.pprint("User is Deactivated.")
        return HttpResponseRedirect(reverse(app + ':user_dashboard',args=(str(id),)))
    except:	
	    return HttpResponseRedirect(reverse(app + ':user_dashboard',args=(str(id),))) 


def user_activate(request,user_id,id):
    usr = User.objects.get(id=id)
    id = usr.id
    user =  User.objects.get(id=user_id)
    try:
        user.is_active = True
        user.save()
        pprint.pprint("User is activated.")
        return HttpResponseRedirect(reverse(app + ':user_dashboard',args=(str(id),)))
    except:	
	    return HttpResponseRedirect(reverse(app + ':user_dashboard',args=(str(id),))) 






def signup(request,id):
    user =  User.objects.get(id=id)
    pprint.pprint(user)
    id = user.id 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(app + ':user_dashboard',args=(str(id),)))
        else:
            return render(request, app + '/signup.html', { 'error':'Opps Check the username and password meets the Criteria...' })
    else:
        form = SignUpForm()
    return render(request, app + '/signup.html', {'form': form, 'user':user, 'error':'Something wrong in the form' })


	
	
	
	
	
   