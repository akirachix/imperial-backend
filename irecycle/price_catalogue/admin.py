from django.contrib import admin

# Register your models here.
from .models import Market, Trader, Agent,FabricCatalogue, ClothesListing
 
    


admin.site.register(Market),

admin.site.register(Trader),

admin.site.register(Agent),

admin.site.register(FabricCatalogue),


admin.site.register(ClothesListing),
