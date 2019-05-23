from django.shortcuts import render, redirect
from .models import Hike, Comments, HikeGroup
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import HikeForm

from django.contrib.auth.models import User
from accounts.models import Profile

# Create your views here.
# HIKE VIEWS

# landing page.
# Missing functionality - hike list and google calender
def landing(request):
  hikes = Hike.objects.all()
  if request.user.is_authenticated:
    user = request.user
    profile = Profile.objects.get(id=user.pk)
    return render(request, 'hike/landing.html', {'profile': profile,'hikes':hikes})
  else:
    return render(request, 'hike/landing.html', {'hikes':hikes})

# show user details about a selected hike.
# Missing functionality - selected hike with map)
def hike_detail(request, hike_id):
  hike = Hike.objects.get(id=hike_id)
  if request.user.is_authenticated:
    user = request.user
    profile = Profile.objects.get(id=user.pk)
    return render(request, 'hike/hike_detail.html', {'profile': profile,'hike':hike})
  else:
    return render(request, 'hike/hike_detail.html', {'hike':hike})

#add a new hike
# create a form to add a new hike

@login_required
def hike_new(request):
  if request.method == 'POST':
    form = HikeForm(request.POST)
    if form.is_valid():
      hike = form.save(commit=False)
      user = request.user
      profile = Profile.objects.get(user=user.pk)
      hike.profile = profile
      hike.save()
      return redirect('hike_detail', hike_id=hike.pk)
  else:
      form = HikeForm()
  return render(request, 'hike/hike_form.html', {'form': form})

# show all hikes on a calendar
def hike_calendar(request):
    hikes = Hike.objects.order_by('hike_date');
    return render(request, 'hike/hike_calendar.html', {'hikes': hikes})

# USER / PROFILE VIEWS
