from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "calculator"


urlpatterns = [
    path("", views.calculator, name="calculator"),
    path("invoice", views.invoice, name="invoice"),
    path("invoice_confirm", views.invoice_confirm, name="invoice_confirm"),
    path("user", views.user_form, name="user_form"),
]
