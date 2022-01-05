from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "calculator"


urlpatterns = [
    path("", views.calculator, name="calculator"),
    path("invoice", views.invoice, name="invoice"),
    path("user", views.user_form, name="user_form"),
]
