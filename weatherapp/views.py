from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from django.contrib import messages

# Create your views here.
def index(request):
    API_KEY= config("API_KEY")
    city="Ankara"
    u_city = request.POST.get("name")
    if u_city:
        url=f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        print(response.ok)
        
        if response.ok:
            pass
        else:
            messages.warning(request, "There is no city" )
    
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    content = response.json()
   
    
    context = {
        "city" : content["name"],
        "temp" : content["main"]["temp"],
        "icon" : content["weather"][0]["icon"],
        "desc" : content["weather"][0]["description"]
    }
    
    
    return render(request, "weatherapp/index.html", context)


