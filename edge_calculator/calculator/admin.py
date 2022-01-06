from django.contrib import admin

# Register your models here.
from .models import Brand, CustomBike, CustomBikeUser

admin.site.register(CustomBike)
admin.site.register(Brand)
admin.site.register(CustomBikeUser)
