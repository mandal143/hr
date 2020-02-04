from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('Login/', views.Login, name='Login'),
    path('Logout/^(?P<id>\w+)/$', views.Logout, name='Logout'),
	path('export_users_csv/$', views.export_users_csv, name='export_users_csv'),
	path('change_password/^(?P<id>\w+)/$', views.change_password, name='change_password'),
	path('change_password_save/^(?P<id>\w+)/$', views.change_password_save, name='change_password_save'),
	path('masterdashboard/^(?P<id>\w+)/$', views.masterdashboard, name='masterdashboard'),
	
]
