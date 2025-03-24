from django.contrib import admin
from .models import Customer, Vehicle, Booking, Payment, Review, LoyaltyPoints
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(LoyaltyPoints)
