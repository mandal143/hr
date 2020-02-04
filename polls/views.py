from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse
from .models import LoginLogoutLog
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django.utils.timezone import localtime, get_current_timezone
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pprint
import csv
import pytz
app = "polls"

def index(request):
    return  render(request,app+'/login.html')
	
def Login(request):
   
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            pprint.pprint("active")
            if user.is_active:
                if user.is_superuser:
                    # user_all = User.objects.all()
                    user_details = LoginLogoutLog.objects.all()
                    return render(request,  app+'/admin.html', {'user_details':user_details, 'user':user})
                else:
                    try:
                        user_id = User.objects.get(id=user.id)
                        user_time = LoginLogoutLog.objects.filter(user=user_id).order_by('-login_time')[0]
                        pprint.pprint(user_time.logout_time)
                        user_previous_time = user_time.logout_time
                        pprint.pprint(user_id)
                        if(user_previous_time == None):
                            pprint.pprint(user_previous_time)
                            context = { 'user_previous_time': 'NOTE:  The "Clock is running" in the time keeping.','user':user }
                            pprint.pprint("sfsdgfiudi")
                            return render(request,  app + '/error.html', context)
                        else:
                            tz = get_current_timezone()
                            started_at_time = timezone.activate(tz)
                            started_at = localtime(started_at_time)
                            pprint.pprint(str(started_at))
                            TodayStartdate = str(started_at)[0:19]
                            LoginLogoutLog.objects.create(user=user,login_time=TodayStartdate)
                            context = { 'user':user }
                            return render(request, app + '/staff.html', context)
                    except:	
                        tz = get_current_timezone()
                        started_at_time = timezone.activate(tz)
                        started_at = localtime(started_at_time)
                        pprint.pprint(str(started_at))
                        TodayStartdate = str(started_at)[0:19]
                        LoginLogoutLog.objects.create(user=user,login_time=TodayStartdate)
                        context = { 'user':user }
                        return render(request, app + '/staff.html', context)
            else:
                pprint.pprint("success2")
                return HttpResponseRedirect(reverse(app + '/login.html'), {'error_message': 'Error: Your account has been disabled'})
        else: 
            pprint.pprint("success3")
            return render(request,  app+'/login.html', {'error_message': 'Error: Invalid login. Please try again!!'})
            
		
def Logout(request,id):
    			
	try:  
		
		user_id = User.objects.get(id=id)
		pprint.pprint(user_id)
		user_time = LoginLogoutLog.objects.filter(user=user_id).order_by('-login_time')[0]		
		tz = get_current_timezone()
		started_at_time = timezone.activate(tz)
		started_at = localtime(started_at_time)
		pprint.pprint(str(started_at))
		TodayEnddate = str(started_at)[0:19]
		pprint.pprint(TodayEnddate)
		user_time.logout_time = TodayEnddate
		user_time.save()
		return HttpResponseRedirect(reverse(app + ':index'))
		
	except Exception as e:
		pprint.pprint("Successfully Logout")
		return HttpResponseRedirect(reverse(app + ':index'))

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Reports.csv"'

    writer = csv.writer(response)
    writer.writerow(['User Name','Login Time Details','Logout Time Details','Remarks',])
    details = LoginLogoutLog.objects.all()
    current_tz = pytz.timezone('Asia/Kolkata')
	
    for detail in details:
        user = detail.user.get_full_name()
        login_ti = detail.login_time
        login_tim = current_tz.normalize(login_ti.astimezone(current_tz))
        login_time = str(login_tim)[0:19]
		
        logout_ti = detail.logout_time
        if(logout_ti == None):
            logout_time = str(logout_ti)
            remarks = detail.remarks
            done = (user,login_time,logout_time,remarks)
            writer.writerow(done) 
        else:
            logout_tim = current_tz.normalize(logout_ti.astimezone(current_tz))
            logout_time = str(logout_tim)[0:19]
            remarks = detail.remarks
            done = (user,login_time,logout_time,remarks)
            writer.writerow(done)

    return response				

def change_password(request,id):
    user = User.objects.get(id=id)
    pprint.pprint(user)
    form = PasswordChangeForm(user)
    pprint.pprint(form)
    return render(request,  app+'/change_password.html', {'user': user, 'form': form})	
	

def change_password_save(request,id):
    
    pprint.pprint("passord change request")
    user = User.objects.get(id=id)
    pprint.pprint(user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user,  data=request.POST)
        pprint.pprint("yes we got")
        pprint.pprint(user)
        if form.is_valid():
            user = form.save()
            pprint.pprint("succeed")
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request, 'polls/password_change_done.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user)
    return render(request, 'polls/change_password.html', {'user': user,'form': form})
	
    	
def masterdashboard(request,id):
    user = User.objects.get(id=id)
    user_time = LoginLogoutLog.objects.filter(user=user).order_by('-login_time')[0]
    pprint.pprint(user_time.logout_time)
    user_previous_time = user_time.logout_time
    pprint.pprint(user)
    if(user_previous_time == None):
        pprint.pprint(user_previous_time)
        pprint.pprint("hey we will see you")
        context = { 'user':user }
        return render(request, app + '/staff.html', context)
    else:
        context = { 'error_message': 'NOTE:  Something Wrong please contact the developer ','user':user }
        pprint.pprint("sfsdgf")
        return render(request,  app + '/error.html', context)