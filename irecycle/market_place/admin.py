from django.contrib import admin

# Register your models here.
from .models import RecyclingCompany, Collection, Payment

admin.site.register(RecyclingCompany),
admin.site.register(Collection),
admin.site.register(Payment),