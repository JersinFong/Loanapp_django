from django.urls import path
from .views import (
	StatusAPIView,
	StatusDetailAPIView,
)
urlpatterns = [
	path('loanapp/', StatusAPIView.as_view(), name='post'),
	path('status/',  StatusAPIView.as_view()),
    path('status/<int:id>/', StatusDetailAPIView.as_view(), name='detail'),
]
app_name = 'status'