from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
  if request.method == "POST":
    city = request.POST["city"]
    res = urllib.request.urlopen("http://api.openweathermap.org/geo/1.0/direct?q=" + city + "&limit=5&appid=197bfc16d8d956cbdf5cf5063aa08489").read()
    json_data = json.loads(res)
    lat = json_data[0]["lat"]
    lon = json_data[0]["lon"]
    wdata = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=197bfc16d8d956cbdf5cf5063aa08489").read()
    json_wdata = json.loads(wdata)
    data = {
      "code": json_wdata["sys"]["country"],
      "humidity": json_wdata["main"]["humidity"],
      "temperature": json_wdata["main"]["temp"],
      "desc": json_wdata["weather"][0]["description"]
    }
  else:
    data = {}
  return render(request, "index.html", {"data": data})
