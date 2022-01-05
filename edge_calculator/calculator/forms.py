from django import forms

from .models import Brand, CustomBike, CustomBikeUser


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomBikeUser
        fields = "__all__"


class CustomBikeForm(forms.ModelForm):
    frame_choice = forms.ModelChoiceField(queryset=Brand.objects.filter(component="FR"))
    wheelset_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="WS")
    )
    drivetrain_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="DT")
    )
    handlebar_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="HB")
    )
    stem_choice = forms.ModelChoiceField(queryset=Brand.objects.filter(component="ST"))
    seatpost_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="SP")
    )
    saddle_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="SA")
    )
    bottombracket_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="BB")
    )
    special_items_choice = forms.ModelChoiceField(
        queryset=Brand.objects.filter(component="SI")
    )

    class Meta:
        model = CustomBike
        fields = [
            "frame_choice",
            "wheelset_choice",
            "drivetrain_choice",
            "handlebar_choice",
            "stem_choice",
            "seatpost_choice",
            "saddle_choice",
            "bottombracket_choice",
            "special_items_choice",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial["frame_choice"] = Brand.objects.first()
        self.initial["wheelset_choice"] = Brand.objects.get(name="None", component="WS")
        self.initial["drivetrain_choice"] = Brand.objects.get(
            name="None", component="DT"
        )
        self.initial["handlebar_choice"] = Brand.objects.get(
            name="None", component="HB"
        )
        self.initial["stem_choice"] = Brand.objects.get(name="None", component="ST")
        self.initial["seatpost_choice"] = Brand.objects.get(name="None", component="SP")
        self.initial["saddle_choice"] = Brand.objects.get(name="None", component="SA")
        self.initial["bottombracket_choice"] = Brand.objects.get(
            name="None", component="BB"
        )
        self.initial["special_items_choice"] = Brand.objects.get(
            name="None", component="SI"
        )


class FrameForm(forms.Form):
    frame = forms.ModelChoiceField(queryset=Brand.objects.filter(component="FR"))

    class Meta:
        model = Brand
        fields = ["frame"]


class WheelsetForm(forms.Form):
    wheel_set = forms.ModelChoiceField(queryset=Brand.objects.filter(component="WS"))
