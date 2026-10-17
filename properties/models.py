from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Property(models.Model):
    PROPERTY_TYPES = [
        ("Apartment", "Apartment"),
        ("House", "House"),
        ("Room", "Room"),
        ("PG", "PG"),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    area_sqft = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    amenities = models.ManyToManyField(
        "properties.Amenity", blank=True, related_name="properties"
    )


    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"


    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(
        "properties.Property", on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="properties/")
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.property.title}"


class Amenity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Amenity"
        verbose_name_plural = "Amenities"

    def __str__(self):
        return self.name
