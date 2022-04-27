from django.contrib import admin
from jmespath import search
from .models import Demand

# Register your models here.


class DemandAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "text")
    list_display_links = ("id", "title")
    search_fields = ("title", "text")


admin.site.register(Demand, DemandAdmin)
    
