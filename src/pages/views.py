from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    obj = {
        "description" : "I want to be a Software Developer.",
        "email" : "developer_din@email.com",
        "number" : "12345654321",
        "hobbies" : ["Playing Video Games", "Watching Movies", "Eating", "Playing Sports"]
    }
    return render(request, "contact.html", obj)

def about_view(request, *args, **kwargs):
     return render(request, "about.html", {})
