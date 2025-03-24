from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    email = models.EmailField()
    phone = models.CharField(max_length=15)  
    loyalty_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Vehicle(models.Model):
    VEHICLE_TYPE = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('luxury', 'Luxury')
    ]

    TRANSMISSION_TYPE = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic')
    ]

    FUEL_TYPE = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric')
    ]

    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=VEHICLE_TYPE)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE)
    transmission = models.CharField(max_length=50, choices=TRANSMISSION_TYPE)
    features = models.TextField(blank=True, null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"


class Booking(models.Model):
    STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    dropoff_location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICE, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.vehicle.model}"


class Payment(models.Model):
    PAYMENT_METHOD = [
        ('credit card', 'Credit Card'),
        ('debit card', 'Debit Card'),
        ('digital wallet', 'Digital Wallet')
    ]

    PAYMENT_STATUS = [
        ('failed', 'Failed'),
        ('success', 'Success')
    ]

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # This must be here
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    status = models.CharField(max_length=50, choices=PAYMENT_STATUS, default='success')
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking.user.username} - {self.amount}"


class Review(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.vehicle.model}"


class LoyaltyPoints(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)  
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.points} points"
