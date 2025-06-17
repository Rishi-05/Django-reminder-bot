from django.urls import path
from .views import ProtectedView

urlpatterns = [
    path('secret/', ProtectedView.as_view(), name='protected'),
]
