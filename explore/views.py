from itertools import count
from django.shortcuts import render
from explore.models import Explore, City
from blog.models import BlogPost
# import pyttsx3
# Create your views here.
def explore(request):
    param = Explore.objects.all()
    context = {'explore':param}
    return render(request, 'explore/page22.html', context)

def city(request, country):
    cityName = City.objects.filter(country = country)
    cities = {'city': cityName}
    return render(request, 'explore/city.html', cities)


def explorePlaces(request, country, city):
    places = BlogPost.objects.all()
    country_name = BlogPost.objects.filter(country = country, city = city)
    msg = country_name.first()
    dict_places = {'explorePl':places, 'country1':country_name,'msg':msg}
    return render(request, 'explore/exploreplaces.html', dict_places)




def Contact(request):
    return render(request, 'home/Contact.html')