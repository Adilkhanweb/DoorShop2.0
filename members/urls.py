from django.urls import path
from members.views import *

urlpatterns = [
    # path('login/', UserLoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', UserRegisterView.as_view(template_name='registration/register.html'), name='register'),
]
