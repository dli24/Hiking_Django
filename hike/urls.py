from django.urls import path
from . import views

urlpatterns = [
  # home url
  path('', views.landing, name='landing'),

  # hike urls

  # show user selected hike ... needs id and user pk
  path('hike', views.hike_detail, name='hike_detail'),

  #add a new hike
  path('hike/new', views.hike_new, name='hike_new'),


]
