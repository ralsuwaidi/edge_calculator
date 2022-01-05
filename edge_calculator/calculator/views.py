# Create your views here.
from django.shortcuts import render

from .forms import CustomBikeForm, UserForm
from .models import Brand, CustomBike, CustomBikeUser


def calculator(request):
    context = {}

    if request.POST:
        form = CustomBikeForm(request.POST)
        if form.is_valid():
            frame_choice = form.cleaned_data["frame_choice"]
            wheelset_choice = form.cleaned_data["wheelset_choice"]
            drivetrain_choice = form.cleaned_data["drivetrain_choice"]
            handlebar_choice = form.cleaned_data["handlebar_choice"]
            stem_choice = form.cleaned_data["stem_choice"]
            seatpost_choice = form.cleaned_data["seatpost_choice"]
            saddle_choice = form.cleaned_data["saddle_choice"]
            bottombracket_choice = form.cleaned_data["bottombracket_choice"]
            special_items_choice = form.cleaned_data["special_items_choice"]

            frame = Brand.objects.get(name=frame_choice, component="FR")
            wheelset = Brand.objects.get(name=wheelset_choice, component="WS")
            drivetrain = Brand.objects.get(name=drivetrain_choice, component="DT")
            handlebar = Brand.objects.get(name=handlebar_choice, component="HB")
            stem = Brand.objects.get(name=stem_choice, component="ST")
            seatpost = Brand.objects.get(name=seatpost_choice, component="SP")
            saddle = Brand.objects.get(name=saddle_choice, component="SA")
            bottombracket = Brand.objects.get(name=bottombracket_choice, component="BB")
            special_items = Brand.objects.get(name=special_items_choice, component="SI")

            custom_bike = CustomBike(
                frame=frame,
                wheelset=wheelset,
                drivetrain=drivetrain,
                handlebar=handlebar,
                stem=stem,
                seatpost=seatpost,
                saddle=saddle,
                bottombracket=bottombracket,
                special_items=special_items,
            )

            price = custom_bike.price
            context["price"] = price

        if "accept_components" in request.POST:
            pass

    else:
        form = CustomBikeForm()

        custom_bike = CustomBike(
            frame=Brand.objects.first(),
            wheelset=Brand.objects.get(name="None", component="WS"),
            drivetrain=Brand.objects.get(name="None", component="DT"),
            handlebar=Brand.objects.get(name="None", component="HB"),
            stem=Brand.objects.get(name="None", component="ST"),
            seatpost=Brand.objects.get(name="None", component="SP"),
            saddle=Brand.objects.get(name="None", component="SA"),
            bottombracket=Brand.objects.get(name="None", component="BB"),
            special_items=Brand.objects.get(name="None", component="SI"),
        )

        price = custom_bike.price
        context["price"] = price

    context["form"] = form
    return render(request, "calculator/home.html", context)


def invoice(request):
    context = {}

    return render(request, "calculator/invoice.html", context)


def user_form(request):

    context = {}

    form = UserForm()
    context["form"] = form

    return render(request, "calculator/user_form.html", context)
