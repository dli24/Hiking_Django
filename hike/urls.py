from django.urls import path
from . import views

urlpatterns = [
  # home url
  path('', views.landing, name='landing'),

  # hike urls

  # show user selected hike ... needs id and user pk
  path('hike/<int:hike_id>', views.hike_detail, name='hike_detail'),

  #add a new hike
  path('hike/new', views.hike_new, name='hike_new'),

  #path('hike/<int:pk>/edit', views.hike_edit, name='hike_edit'),

  # show hike calendar
  path('hike/calendar', views.hike_calendar, name='hike_calendar'),

  # add a comment to a hike
  path('hike/comment/<int:pk>', views.comment_new, name='comment_new'),

  # add user to hike
  path('hike/join/<int:pk>', views.hike_join, name='hike_join'),
]
