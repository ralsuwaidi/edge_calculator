from django.db import models
from django.db.models.base import Model
from django.utils.translation import gettext_lazy as _

# Create your models here.


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
