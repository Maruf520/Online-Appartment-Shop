from django.contrib import admin

from . models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_filter = ('realtor',)
    search_fields = ('title','description','price', 'city', 'zipcode','address')

admin.site.register(Listing, ListingAdmin)
