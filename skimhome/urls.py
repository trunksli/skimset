from django.urls import path, include, re_path
from . import views
from skimhome import views

app_name = 'skimhome'

urlpatterns = [
	path('', views.home, name='home'),
	#path('createaccount/', views.createaccount, name='createaccount'),
	#path('login/', views.login, name='login'),
	#path('aboutus/', views.aboutus, name='aboutus'),
]

