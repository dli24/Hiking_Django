from django.shortcuts import render, redirect
from .models import Hike, Comments, HikeGroup
from django.contrib.auth.decorators import login_required
from .models import Hike

# Create your views here.
# HIKE VIEWS

# landing page.
# Missing functionality - hike list and google calender
def landing(request):
  hikes = Hike.objects.all()
  return render(request, 'hike/landing.html', {'hikes':hikes})

# show user details about a selected hike.
# Missing functionality - selected hike with map)
def hike_detail(request):
  return render(request, 'hike/hike_detail.html')

#add a new hike
# create a form to add a new hike
def hike_new(request):
  return render(request, 'hike/hike_new.html')

# show all hikes on a calendar
def hike_calendar(request):
    return render(request, 'hike/hike_calendar.html')

# USER / PROFILE VIEWS
