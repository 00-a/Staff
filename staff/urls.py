from django.urls import path

from .views import StaffListView, EmployeeDetailView, EmployeeCreateView

urlpatterns = [
    path('staff/', StaffListView.as_view()),
    path('staff/<int:pk>', EmployeeDetailView.as_view()),
    path('staff/create', EmployeeCreateView.as_view())
]