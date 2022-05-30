from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TestPurchase, GiftsPurchase, Consult, OrderHistory
import datetime


def time_please():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 12:
        return 'Good morning'
    elif 12 <= hour < 18:
        return 'Good afternoon'
    else:
        return 'Good evening'


# Create your views here.


class PortalView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    redirect_field_name = 'portal/portal.html'
    template_name = 'portal/portal.html'
    context_object_name = 'latest_purchases'
    model = TestPurchase

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.email
        context['purchases'] = TestPurchase.objects.filter(user=self.request.user)
        context['time_greeting'] = time_please()

        return context


class TestsView(ListView):
    model = TestPurchase
    template_name = 'portal/tests.html'
    context_object_name = 'user_tests'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['purchases'] = TestPurchase.objects.filter(user=self.request.user)
        return context

    # def get_queryset(self):
    #
    #     self.user = get_object_or_404(TestPurchase, user=self.kwargs['user'])
    #
    #     return TestPurchase.objects.filter(user=self.user)


class ConsultsView(ListView):
    template_name = 'portal/consults.html'
    context_object_name = 'latest_purchases'

    def get_queryset(self):
        return Consult.objects.order_by('-time_scheduled')


class OrderHistoryView(ListView):
    template_name = 'portal/history.html'
    context_object_name = 'latest_purchases'

    def get_queryset(self):
        return OrderHistory.objects.all()


class SupportView(ListView):
    template_name = 'portal/support.html'
    context_object_name = 'latest_purchases'

    def get_queryset(self):
        return OrderHistory.objects.all()


class SettingsView(ListView):
    template_name = 'portal/settings.html'
    context_object_name = 'latest_purchases'

    def get_queryset(self):
        return OrderHistory.objects.all()


class EmailView(ListView):
    template_name = 'portal/email.html'
    context_object_name = 'latest_purchases'

    def get_queryset(self):
        return OrderHistory.objects.all()


class PasswordChangeView(ListView):
    template_name = 'portal/password.html'
    context_object_name = 'latest_purchases'

    def get_queryset(self):
        return OrderHistory.objects.all()
