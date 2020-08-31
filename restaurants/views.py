from django.shortcuts import render,redirect
from .forms import RestaurantForm
from .models import Restaurant

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form =RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("restaurant-list")

    context = {
    "form":form,
     }
    return render(request, 'create.html', context)
# Create a form for creating Restaurant objects.
# Your form should be in a forms.py file.
# Your form should be called RestaurantForm.
# Your form should include all of the fields.
# Complete the restaurant_create view so that it can be used to allow users to create Restaurant objects.
# After successfully creating an object the user should be redirected to another page.
# Complete the HTML file provided, so that the user input can be taken and handled properly.
# The URL has been written for you so you don't need to create one.
# Pass the tests.
# Push your code.
