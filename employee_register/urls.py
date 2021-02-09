from django.urls import path, include
from . import views
from employee_register.views import EmployeeList, EmployeeFormView
urlpatterns = [
    #path('', views.employee_form,name='employee_insert'), #get and post.req for insert operation.
    path('', EmployeeFormView.as_view(),name='employee_insert'),
    #path('<int:id>/',views.employee_form,name='employee_update'), #get and post.req for update operation.
    #path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    #path('list/', views.employee_list,name='employee_list')
    path('list/',EmployeeList.as_view(),name='employee_list'),
]