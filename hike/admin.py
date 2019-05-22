from django.contrib import admin

# Register your models here.
from .models import Hike, Comments, HikeGroup

admin.site.register(Hike)
admin.site.register(Comments)
admin.site.register(HikeGroup)