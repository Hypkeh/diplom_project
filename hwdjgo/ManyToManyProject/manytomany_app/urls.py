from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.StudentList.as_view(), name='student_list')
]