from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Location

# Create your views here.
def view_map(request):
    return render(request, "feed/map.html")

def add_location(request):
    if request.method == "POST":
        print(request.POST)
        longitude = request.POST["long"]
        latitude = request.POST["lat"]
        desc = request.POST["desc"]
        pet_type = request.POST["type"]

        Location.objects.create(longitude=longitude, latitude=latitude, description=desc, pet_type=pet_type)

        return redirect("/feed/map")
    else:
        return render(request, "feed/add.html")

def fetch_locations(request):
    data = []
    for loc in Location.objects.all():
        pet_type = loc.pet_type.lower()
        if pet_type == "dog":
            icon = "https://res.cloudinary.com/boyuan12/image/upload/v1714274574/dog_lupe3z.png"
        elif pet_type == "cat":
            icon = "https://res.cloudinary.com/boyuan12/image/upload/v1714272569/cat_1_fpacpr.png"
        data.append({"long": float(loc.longitude), "lat": float(loc.latitude), "icon": icon, "desc": loc.description})
    return JsonResponse(data, safe=False)
