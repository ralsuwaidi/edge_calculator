from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "calculator"


urlpatterns = [
    path("", views.calculator, name="calculator"),
    path("wheelset", views.choose_wheelset, name="choose_wheelset"),
    # path("", TemplateView.as_view(template_name="calculator/home.html"), name="home"),
]
