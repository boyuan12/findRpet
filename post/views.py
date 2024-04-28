import os

import cloudinary
import cloudinary.api
import cloudinary.uploader

from django.shortcuts import render, redirect
from django.views.generic import ListView

from authentication.models import Profile
from .models import Post


cloudinary.config(
    cloud_name=os.environ.get("CLOUD_NAME"),
    api_key=os.environ.get("CLOUD_API_KEY"),
    api_secret=os.environ.get("CLOUD_API_SECRET"),
    secure=True)

# # Create your views here.
# class Pets(ListView):
#     model = Post
#     template_name = "post/scroll_page.html"
#     context_object_name = "pets"
#     paginate_by = 3
#     def get_template_names(self, *args, **kwargs):
#         if self.request.htmx:
#             return "post/pets_list.html"
#         else:
#             return self.template_name

def scroll_page(request):
    all_pets = Post.objects.all()
    print(all_pets)
    return render(request, "post/scroll_page.html", {"all_pets": all_pets})

def pet_page(request, pk):
    pet_profile = Post.objects.get(pk=pk)
    owner_profile = Profile.objects.get(user=pet_profile.user)
    print(owner_profile.phone_number)
    return render(request, "post/pet_page.html", {"pet_profile": pet_profile, "owner": owner_profile})

def make_post(request):
    if request.method == 'POST':
        image_response = cloudinary.uploader.upload(request.FILES['pet_picture'])
        img_url = image_response["secure_url"]

        Post.objects.create(
            user=request.user,
            pet_name=request.POST["pet_name"],
            pet_description=request.POST["pet_description"],
            pet_picture=img_url,
            status=False
        )
        return redirect("scroll_page")
    else:
        return render(request, "post/make_post.html")

def found(request, pk):
    pet_profile = Post.objects.get(id=pk)
    pet_profile.status = True
    pet_profile.save()
    return redirect("/")