from django.urls import include, path
from .views import *
urlpatterns = [
    # other URL patterns here
    path('', getData),
]