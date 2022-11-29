from django.urls import path

from .views import *

urlpatterns = [
    path('/<int:c>/<int:s>/<str:p_slug/', detail),
    path('list/', listing),
]
