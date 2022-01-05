from django.core.validators import RegexValidator
from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomBikeUser(models.Model):
    ABUDHABI = "AD"
    DUBAI = "DB"
    SHARJAH = "SH"
    AJMAN = "AJ"
    UMMALQUWAIN = "UQ"
    RASALKAIMAH = "RK"
    FUJAIRAH = "FU"
    EMIRATES_CHOICES = [
        (ABUDHABI, "Abu Dhabi"),
        (DUBAI, "Dubai"),
        (SHARJAH, "Sjarjah"),
        (AJMAN, "Ajman"),
        (UMMALQUWAIN, "Umm Al Quwain"),
        (RASALKAIMAH, "Ras Al Khaimah"),
        (FUJAIRAH, "Fujairah"),
    ]

    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email"))
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,9}$",
        message="Phone number must be entered in the format: '+50XXXXXXX'.",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True
    )  # validators should be a list
    street_adress = models.CharField(_("Street Adress"), max_length=200)
    area = models.CharField(_("Area"), max_length=200)
    city = models.CharField(choices=EMIRATES_CHOICES, default=DUBAI, max_length=2)


class Brand(models.Model):
    FRAME = "FR"
    WHEELSET = "WS"
    DRIVETRAIN = "DT"
    HANDLEBAR = "HB"
    STEM = "ST"
    SEATPOST = "SP"
    SADDLE = "SA"
    BOTTOMBRACKET = "BB"
    SPECIAL_ITEM = "SI"
    COMPONENT_CHOICES = [
        (FRAME, "Frame"),
        (WHEELSET, "Wheel Set"),
        (DRIVETRAIN, "Drive Train"),
        (HANDLEBAR, "Handle Bar"),
        (STEM, "Stem"),
        (SEATPOST, "Seat Post"),
        (SADDLE, "Saddle"),
        (BOTTOMBRACKET, "Bottom Bracket"),
        (SPECIAL_ITEM, "Special Item"),
    ]

    name = models.CharField(_("Brand name"), max_length=255)
    full_price = models.DecimalField(_("Full price"), max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(
        _("Discounted price"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    discount_amount = models.IntegerField(
        _("Discount in percentage"), blank=True, null=True
    )
    component = models.CharField(choices=COMPONENT_CHOICES, default=FRAME, max_length=2)

    def __str__(self) -> str:
        return self.name

    @property
    def price(self):
        return self.discounted_price or self.full_price


class CustomBike(models.Model):
    frame = models.ForeignKey(Brand, related_name="frame", on_delete=models.CASCADE)
    wheelset = models.ForeignKey(
        Brand, related_name="wheelset", on_delete=models.CASCADE
    )
    drivetrain = models.ForeignKey(
        Brand, related_name="drivetrain", on_delete=models.CASCADE
    )
    handlebar = models.ForeignKey(
        Brand, related_name="handlebar", on_delete=models.CASCADE
    )
    stem = models.ForeignKey(Brand, related_name="stem", on_delete=models.CASCADE)
    seatpost = models.ForeignKey(
        Brand, related_name="seatpost", on_delete=models.CASCADE
    )
    saddle = models.ForeignKey(Brand, related_name="saddle", on_delete=models.CASCADE)
    bottombracket = models.ForeignKey(
        Brand, related_name="bottombracket", on_delete=models.CASCADE
    )
    special_items = models.ForeignKey(
        Brand, related_name="special_items", on_delete=models.CASCADE
    )

    @property
    def price(self):
        return (
            self.frame.price
            + self.wheelset.price
            + self.drivetrain.price
            + self.handlebar.price
            + self.stem.price
            + self.seatpost.price
            + self.saddle.price
            + self.bottombracket.price
            + self.special_items.price
        )
