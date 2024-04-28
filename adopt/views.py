from django.http import JsonResponse
from django.shortcuts import render
import requests

# Create your views here.
def add_adoption(request):
    if request.method == "POST":
        pass

def view_adoptable_animals(request):
    if request.GET["p"]:
        result, total, current = api_petfinder(p=request.GET["p"], lat=request.GET["lat"], long=request.GET["long"])
        return render(request, "adopt/index.html", {
            "results": result,
            "total": total,
            "start": current * 3 - 2,
            "end": current * 3,
            "current": current,
            "prev": current - 1,
            "next": current + 1
        })
    
    result, total, current = api_petfinder(lat=request.GET["lat"], long=request.GET["long"])
    return render(request, "adopt/index.html", {
            "results": result,
            "total": total,
            "start": current * 3 - 2,
            "end": current * 3,
            "current": current,
            "prev": current - 1,
            "next": current + 1  
    })

def search_adoptable_animals(request):
    return render(request, "adopt/search.html")
    
def api_petfinder(lat, long, p=1):
    data = requests.get(f"https://api.petfinder.com/v2/animals?tlocation={lat},{long}&limit=3&page={p}", headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJtd1NmUDQ1SEpPckFSS0RkVGM1M3JGSjNHVTJIdnk0SUxVSGR5Y3NnNGpURzRCVHIzdCIsImp0aSI6ImplcUdCb2VDRHB4ZmFvc3BDMDN3d0wzb05PakhMemJDUXhyWHFpQlgiLCJpYXQiOjE3MTQyOTA3ODgsIm5iZiI6MTcxNDI5MDc4OCwiZXhwIjo0ODY5OTY0Mzg4LCJzdWIiOiIxNjg0ODgwNyIsInNjb3BlcyI6W119.TibrpCmqDsVTRf8sKcbbZuYyv6S9pgbJpXqS269NZr4TZiYcpzGBWi1zjnOL9Y4r8LCCrY9hKWv7xbVbMSFiIxhw8XryMQePYsLWu7MFuFbONyI7vvjt0geLDCTRsMPQpDBd3gSemuBVvyilv7HknDYAIvnk0vWjG1aWazwU9mjN_oBiG8E6hLZXpOwmFk8odZGl0I52sEgoya_62-H_GqtvKFNRo-LJrJwfBjzs5oi1SmPzuyp6E9myCCqLqcLV6NkOgjqTneUY8yxbgwWzaiLkpF-VxZfiKyfX2OvU5V2wML0fDSAr5WEZrCFtoAM2cPFvyUSjRXzKmzfHOyNDHw"
    })

    results = []
    for animal in data.json()["animals"]:
        try:
            results.append({"name": animal["name"], "photo": animal["photos"][0]["small"], "url": animal["url"], "desc": animal["description"]})
        except IndexError:
            results.append({"name": animal["name"], "photo": None, "url": animal["url"]})
    return results, data.json()["pagination"]["total_count"], data.json()["pagination"]["current_page"]


