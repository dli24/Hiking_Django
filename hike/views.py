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
  comments = Comments.objects.filter(hike=hike_id)
  hike_group = HikeGroup.objects.select_related('profile__user').filter(hike=hike_id)
  if request.user.is_authenticated:
    user = request.user
    profile = Profile.objects.get(user=user.pk)
    return render(request, 'hike/hike_detail.html', {'profile': profile,'hike':hike, 'comments': comments, 'user': user, 'hike_group': hike_group})
  else:
    return render(request, 'hike/hike_detail.html', {'hike':hike, 'hike_group': hike_group, 'comments': comments})

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

@login_required
def hike_edit(request, pk):
    hike = Hike.objects.get(pk=pk)
    if request.method == 'POST':
        form = HikeForm(request.POST or None, instance=hike)
        # print("++++++++++IF POST++++++++++")
        if form.is_valid():
            form.save()
            # hike = form.save(commit=False)
            # print("++++++++++IF VALID++++++++++")
            # hike.save()
            return redirect('hike_detail')
    else:
        form = HikeForm(instance=Hike)
    print("++++++++++ELSE++++++++++")
    print("++++++++++RETURN++++++++++")
    return render(request, 'hike/hike_form.html', {'form': form, 'hike':hike})

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
   hikegroup = HikeGroup.objects.create(hike=hike, profile=profile)
   hikegroup.save()

   print(hikegroup.hike, "HikeGroup.hike")
   print(hikegroup.profile, "HikeGroup.profile")
   return redirect('hike_detail', hike_id=pk)

