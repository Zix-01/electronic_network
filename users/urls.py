from django.urls import path
from .views import ActiveEmployeesView

urlpatterns = [
    path('active-employees/', ActiveEmployeesView.as_view(), name='active-employees'),
]
