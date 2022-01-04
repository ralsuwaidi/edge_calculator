# Create your views here.
from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FrameForm, WheelsetForm

frame_g = None
wheel_set_g = None


def calculator(request):
    context = {}

    if request.POST and frame_g == None:
        form = FrameForm(request.POST)
        if form.is_valid():
            frame = form.cleaned_data["frame"]
            print(frame)

        return render(request, "calculator/home.html", context)

    if request.POST and wheel_set_g == None:
        form = WheelsetForm()
        frame = form["frame"]
        print(frame)
        return render(request, "calculator/home.html", context)

    form = FrameForm()
    context["form"] = form
    return render(request, "calculator/home.html", context)


def choose_wheelset(request):

    context = {}
    form = WheelsetForm()

    context["form"] = form
    return render(request, "calculator/home.html", context)
