# https://getbootstrap.com/docs/4.3/getting-started/introduction/

from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.employee_form,name="employee_insert"), #get and post request for insert operation 
    path('<int:id>/',views.employee_form,name="employee_update"), #get and post request for update operation
    path('list/',views.employee_list,name="employee_list"), 
    path('delete/<int:id>/',views.employee_delete,name="employee_delete"), 
]
