from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choice import price_choices, bedroom_choices,city_choices
def index (request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]


    context = {
        'listings' : listings,
        'price_choices':price_choices,
		'bedroom_choices':bedroom_choices,
		'city_choices':city_choices
    }
    return render (request,'pages/index.html', context)

def about (request):
    #Get all Realtors
    realtors = Realtor.objects.order_by('-hire_date')
    
    #Get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)

    context = {
       'realtors' : realtors,
       'mvp_realtors' : mvp_realtors

        
   }


    return render(request,'pages/about.html', context)