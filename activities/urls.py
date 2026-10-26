
from django.urls import path
from .views import StudentListCreateView, StudentSummaryView

urlpatterns = [
    path('activities/', StudentListCreateView.as_view(), name='activities'),
    path('summary/', StudentSummaryView.as_view(), name='summary'),
]
