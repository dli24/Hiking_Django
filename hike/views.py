from django.shortcuts import render, redirect
from .models import Hike, Comments, HikeGroup
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from .forms import HikeForm, CommentForm

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
    profile = Profile.objects.get(user=user.pk)
    return render(request, 'hike/landing.html', {'profile': profile,'hikes':hikes})
  else:
    return render(request, 'hike/landing.html', {'hikes':hikes})

# show user details about a selected hike.
# Missing functionality - selected hike with map)
def hike_detail(request, hike_id):
  hike = Hike.objects.get(id=hike_id)
  if request.user.is_authenticated:
    user = request.user
    profile = Profile.objects.get(user=user.pk)
    comments = Comments.objects.filter(hike=hike_id)
    hike_group = HikeGroup.objects.filter(hike=hike_id)
    return render(request, 'hike/hike_detail.html', {'profile': profile,'hike':hike, 'comments': comments, 'user': user})
  else:
    return render(request, 'hike/hike_detail.html', {'hike':hike})

#add a new hike
# create a form to add a new hike

@login_required
def hike_new(request):
  user = request.user
  profile = Profile.objects.get(user=user.pk)
  if request.method == 'POST':
    form = HikeForm(request.POST)
    if form.is_valid():
      hike = form.save(commit=False)
      hike.profile = profile
      hike.save()
      return redirect('hike_detail', hike_id=hike.pk)
  else:
      form = HikeForm()
  return render(request, 'hike/hike_form.html', {'form': form, 'profile': profile})

# @login_required
# def hike_edit(request, pk):
#   #hike = Hike.objects.get(pk=pk)
#   hike = get_object_or_404(Hike, pk=pk)
#   user = request.user
#   profile = Profile.objects.get(user=user.pk)

#   print(hike.title,  "==================HIKE TITLE==================")
#   print(hike.description, "==================HIKE.DESCRIPTION==================")
#   print(user, "=========THIS USER==========")
#   print(hike.profile, "==========THIS IS HIKE PROFILE==========")

#   if request.method == "POST":
#     form = HikeForm(request.POST, instance=hike)
#     hike = request.hike.copy()
#     if form.is_valid():
#       hike = form.save(commit=False)
#       hike.profile = profile
#       hike.save()
#       return redirect('hike_detail', hike_id=hike.pk)
#   else:
#     form = HikeForm(instance=hike)
#   return render(request, 'hike/hike_form.html', {'form': form, 'profile': profile})


# show all hikes on a calendar
def hike_calendar(request):
    hikes = Hike.objects.order_by('hike_date')
    if request.user.is_authenticated:
        user = request.user
        profile = Profile.objects.get(user=user.pk)
        return render(request, 'hike/hike_calendar.html', {'profile': profile, 'hikes': hikes})
    else:
        return render(request, 'hike/hike_calendar.html', {'hikes': hikes})

#add a comment
@login_required
def comment_new(request, pk):
    hike = Hike.objects.get(pk=pk)
    user = request.user
    profile = Profile.objects.get(user=user.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
          comment = form.save(commit=False)
          comment.profile = profile
          comment.hike = hike
          comment.save()
          return redirect('hike_detail', hike_id=pk)
    else:
        form = CommentForm()
    return render(request, 'hike/comment_form.html', {'form': form, 'hike': hike, 'profile': profile})

def comment_detail(request, hike_id):
  comment = Comments.objects.get(id=hike_id)
  if request.user.is_authenticated:
    user = request.user
    profile = Profile.objects.get(id=user.pk)
    return render(request, 'hike/hike_detail.html', {'hike': hike,'comment':comment, 'profile': profile})
  else:
    return render(request, 'hike/hike_detail.html', {'hike':hike})


@login_required
def hike_join(request, pk):
   hike = Hike.objects.get(pk=pk)
   user = request.user
   profile = Profile.objects.get(user=user.pk)
   HikeGroup.profile = profile
   HikeGroup.hike = hike
   #HikeGroup.save()
   print(HikeGroup.hike,  "HikeGroup.hike")
   print(HikeGroup.profile, "HikeGroup.profile")

   return render(request, 'hike/hike_detail.html', {'hike': hike, 'user':user, 'HikeGroup':HikeGroup})
  
# @login_required
# def hike_unjoin(request, pk):