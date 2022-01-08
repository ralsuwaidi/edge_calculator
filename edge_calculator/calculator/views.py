# Create your views here.
from django.shortcuts import redirect, render

from .forms import ChooseUserForm, CustomBikeForm, UserForm
from .models import Brand, CustomBike

user_g = None
bike_g = None


def calculator(request):
    global bike_g
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

            price = custom_bike.display_price
            context["price"] = price

        if "accept_components" in request.POST:
            bike_g = custom_bike

            return redirect("calculator:user_form")

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

        price = custom_bike.display_price
        context["price"] = price

    context["form"] = form
    return render(request, "calculator/home.html", context)


def user_form(request):
    global user_g, bike_g
    context = {}

    if request.POST:
        form = UserForm(request.POST or None)
        if form.is_valid():
            user_g = form.save(commit=False)
            return redirect("calculator:invoice")

    form = UserForm(request.POST or None)
    context["form"] = form
    context["bike"] = bike_g

    return render(request, "calculator/user_form.html", context)


def invoice(request):
    global user_g, bike_g

    context = {}
    context["user"] = user_g
    context["bike"] = bike_g
    print(bike_g)

    return render(request, "calculator/invoice.html", context)


def invoice_confirm(request):
    global user_g, bike_g

    # save user and bike
    user_g.save()
    bike_g.save()

    context = {}
    context["user"] = user_g
    context["bike"] = bike_g
    context["confirm"] = True

    # reset globals
    user_g = None
    bike_g = None

    return render(request, "calculator/invoice.html", context)
