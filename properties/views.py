from django.shortcuts import render
from .models import Property


def home(request):
    city = request.GET.get("city", "").strip()

    properties = Property.objects.filter(
        is_available=True
    )

    if city:
        properties = properties.filter(city__icontains=city)

    properties = (
        properties
        .prefetch_related("images")
        .order_by("-created_at")[:6]
    )

    return render(
        request,
        "properties/home.html",
        {
            "properties": properties,
            "city": city,
        },
    )
