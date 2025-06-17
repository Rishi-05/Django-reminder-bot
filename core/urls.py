from django.urls import path
from .views import ProtectedView
from .views import home_view

urlpatterns = [
    path('secret/', ProtectedView.as_view(), name='protected'),
    path('', home_view, name='home'),
]
