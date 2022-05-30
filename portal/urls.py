from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required

app_name = 'portal'
urlpatterns = [
    path('', login_required(views.PortalView.as_view()), name='portal'),
    path('tests/', views.TestsView.as_view(), name='tests'),
    path('consults/', views.ConsultsView.as_view(), name='consults'),
    path('orderhistory/', views.OrderHistoryView.as_view(), name='history'),
    path('support/', views.SupportView.as_view(), name='support'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/email/', views.EmailView.as_view(), name='email'),
    path('settings/password/', views.PasswordChangeView.as_view(), name='password')
]
