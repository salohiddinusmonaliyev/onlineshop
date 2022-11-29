from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', profile),
    path('address/', address),
    path('order/', order),
    path('wishlist/', wishlist),
    path('selling/', selling),
    path('setting/', setting),
    path('login/', login_s),
    path('logout/', logout_a),
    path('register/', register)
]
