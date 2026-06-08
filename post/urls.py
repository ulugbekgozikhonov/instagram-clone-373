from django.urls import path
from .views import post_list_view, post_tesha_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('tesha/', post_tesha_view, name='post_tesha'),
]
