from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('create-an-account', views.register, name='register'),
    path('forgot-your-password', views.forgot_password, name='forgot_password'),
]
