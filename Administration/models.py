from django.db import models
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm



# Create your models here.

class Enquiries(models.Model):

    enquiry_id = models.AutoField(primary_key=True)
    enquiry_date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    emp_code = models.CharField(max_length=2500, default='')
    dpr_no = models.CharField(max_length=2500, default='')
    dpr_month = models.CharField(max_length=2500,default='')
    pros_name = models.CharField(max_length=5000,default='')
    pros_date = models.CharField(max_length=5000,default='')
    pros_month = models.CharField(max_length=5000,default='')
    pros_year = models.CharField(max_length=5000,default='')
    enquiry_by = models.CharField(max_length=5000,default='')
    relation = models.CharField(max_length=5000,default='')
    phone1 = models.CharField(max_length=5000,default='')
    phone2 = models.CharField(max_length=5000,default='')
    pros_state = models.CharField(max_length=5000,default='')
    pros_city = models.CharField(max_length=5000,default='')
    pros_course = models.CharField(max_length=5000,default='')
    pros_other = models.CharField(max_length=5000,default='')
    pros_interest_states_1 = models.CharField(max_length=5000,default='')
    pros_interest_states_2 = models.CharField(max_length=5000,default='')
    pros_interest_states_3 = models.CharField(max_length=5000,default='')
    pros_10_marks = models.CharField(max_length=5000,default='')
    pros_12_marks = models.CharField(max_length=5000,default='')
    pros_subject_1 = models.CharField(max_length=5000,default='')
    pros_subject_2 = models.CharField(max_length=5000,default='')
    pros_subject_3 = models.CharField(max_length=5000,default='')
    pros_entrance_exam1 = models.CharField(max_length=5000,default='')
    pros_entrance_exam2 = models.CharField(max_length=5000,default='')
    pros_entrance_exam3 = models.CharField(max_length=5000,default='')
    pros_entrance_exam4 = models.CharField(max_length=5000,default='')
    pros_budget = models.CharField(max_length=5000,default='')
    pros_register_date = models.CharField(max_length=5000,default='')
    pros_register_month = models.CharField(max_length=5000,default='')
    pros_register_year = models.CharField(max_length=5000,default='')
    pros_register_remarks = models.CharField(max_length=5000,default='')
	
    def __str__(self):
        return str(self.enquiry_id)


class Holidays(models.Model):

    holiday_id = models.AutoField(primary_key=True)
    holiday_no= models.CharField(max_length=2500, default='')
    holiday_date = models.CharField(max_length=2500, default='')
    holiday_day = models.CharField(max_length=2500, default='')
    holiday_reason = models.CharField(max_length=2500,default='')
	
    def __str__(self):
        return str(self.holiday_id)
		
class Notices(models.Model):

    notice_id = models.AutoField(primary_key=True)
    notice_date = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    notice_no= models.CharField(max_length=2500, default='')
    notice_details = models.CharField(max_length=2500, default='')
	
    def __str__(self):
        return str(self.notice_id)
		
		
class Grievances(models.Model):
    
	grievance_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	grievance_dated = models.DateTimeField(auto_now_add=True, null=True,blank=True)
	grievance_details = models.CharField(max_length=2500, default='')
	
	def __str__(self):
	    return str(self.grievance_id)
		
class Leaves(models.Model):
   
    leaves_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    leave_dated = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    leave_no_of_days = models.CharField(max_length=2500, default='')
    leave_from_date = models.DateField(null=True,blank=True)
    leave_to_date = models.DateField(null=True,blank=True)
    leave_reason = models.CharField(max_length=2500, default='')
    leave_status = models.CharField(max_length=2500, default='Approval Pending')
	
    def __str__(self):
	    return str(self.leaves_id)
		
class Payrolls(models.Model):
    
    payroll_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pay_month = models.CharField(max_length=2500, default='')
    gross_salary = models.CharField(max_length=2500, default='')
    no_of_leaves = models.CharField(max_length=2500, default='')
    loss_of_amount = models.CharField(max_length=2500, default='')
    advance_salary = models.CharField(max_length=2500, default='')
    net_salary = models.CharField(max_length=2500, default='')
    status = models.CharField(max_length=2500, default='')
	
    def __str__(self):
	    return str(self.payroll_id)
	

class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)    