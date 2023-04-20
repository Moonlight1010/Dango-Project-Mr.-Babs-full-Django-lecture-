from django.urls import path
from .views import register, login, logout_view, 

urlpatterns = [
    path('', register, name='register-page'),
    path('login/', login, name='login-page'),
    path('logout/', logout_view, name='logout-page'),
]