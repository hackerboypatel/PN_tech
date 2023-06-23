from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Restaurant
import json
# Create your views here.

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants})

def search(request):
    if request.method == 'POST':
        searched_query = request.POST['query-search']
        names = Restaurant.objects.filter(name__icontains=searched_query)
        locations = Restaurant.objects.filter(location__icontains=searched_query)
        ids = Restaurant.objects.filter(id__icontains=searched_query)
        lat_long = Restaurant.objects.filter(lat_long__icontains=searched_query)
        data = {
            "searched_query": searched_query,
            "names": names,
            "locations": locations,
            "ids": ids,
            "lat_long": lat_long,
        }
        return render(request, 'search.html', {"data": data})
    else:
        messages.error(request, 'Invalid request. Please submit the search form.')
        return render(request, 'index.html', {'restaurants': restaurants})


def items(request, ids):
    restaurant = Restaurant.objects.get(id=ids)
    items_data = restaurant.items

    if isinstance(items_data, str):
        items_dict = json.loads(items_data)
    else:
        items_dict = items_data

    items_list = [(item_name, item_price) for item_name, item_price in items_dict.items()]

    return render(request, 'items.html', {"restaurant": restaurant,
                                           "items_list": items_list})

def details(request, ids):
    restaurant = Restaurant.objects.get(id=ids)
    details_data = restaurant.full_details

    if isinstance(details_data, str):
        details_dict = json.loads(details_data)
    else:
        details_dict = details_data

    detail_name = details_dict.get("name", "")
    detail_offers = details_dict.get("offers", [])
    detail_cuisines = details_dict.get("cuisines", "")
    detail_currency = details_dict.get("currency", "")
    detail_location = details_dict.get("location", {}).get("locality_verbose", "")
    detail_address = details_dict.get("location", {}).get("address", "")
    detail_city_id = details_dict.get("location", {}).get("city_id", "")
    detail_zipcode = details_dict.get("location", {}).get("zipcode", "")
    detail_latitude = details_dict.get("location", {}).get("latitude", "")
    detail_longitude = details_dict.get("location", {}).get("longitude", "")
    detail_locality = details_dict.get("location", {}).get("locality", "")
    detail_locality_verbose = details_dict.get("location", {}).get("locality_verbose", "")
    detail_country_id = details_dict.get("location", {}).get("country_id", "")
    details_list = [(detail_name, detail_offers, detail_cuisines, detail_currency, detail_location, detail_address, detail_city_id, detail_zipcode, detail_latitude,detail_longitude, detail_locality, detail_locality_verbose, detail_country_id)]
    # Added details only till location
    return render(request, 'details.html', {"details_list": details_list,
                                             "restaurant" : restaurant})
