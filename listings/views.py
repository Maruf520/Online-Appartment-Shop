from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choice import price_choices, bedroom_choices,city_choices
from .models import Listing

def index(request):
	Listings = Listing.objects.all()
	paginator = Paginator(Listings, 3)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)

	context = {
		'Listings' : paged_listings
	}


	return render (request,'listing/listings.html', context)
	
def listing(request, listing_id):
	listing = get_object_or_404(Listing, pk = listing_id)
	context = {
		'listing': listing
	}
	return render(request,'listing/listing.html',context)

def search(request):
	qureyset_list = Listing.objects.order_by('-list_date')

	#Keywords
	if 'keywords' in request.GET:
		keywords  = request.GET['keywords']
		if keywords:
			qureyset_list= qureyset_list.filter(description__icontains=keywords)
	#City
	if 'city' in request.GET:
		city  = request.GET['city']
		if city:
			qureyset_list= qureyset_list.filter(city__iexact=city)
	
	#bedrooms
	if 'bedrooms' in request.GET:
		bedrooms  = request.GET['bedrooms']
		if bedrooms:
			qureyset_list= qureyset_list.filter(bedrooms__lte=bedrooms)		

	 #price
	if 'price' in request.GET:
		price  = request.GET['price']
		if price:
			qureyset_list= qureyset_list.filter(price__lte=price)		

	context = {
		 'price_choices':price_choices,
		'bedroom_choices':bedroom_choices,
		'city_choices':city_choices,
		'Listings': qureyset_list 
	}

	return render(request,'listing/search.html',context)

	