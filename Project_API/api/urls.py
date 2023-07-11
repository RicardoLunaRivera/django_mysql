from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path('employees/', EmployeeView.as_view(), name='employees_list'),
    path('employees/<int:id>', EmployeeView.as_view(), name='employees_process')
]
