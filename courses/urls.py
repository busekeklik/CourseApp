from django.urls import path
from . import views

#http://127.0.0.1:8000/anasayfa/   anasayfa
#http://http://127.0.0.1:8000/     anasayfa
#http://http://127.0.0.1:8000/courses/    courses



urlpatterns = [
    path("", views.home),
    path("anasayfa/", views.home),
    path("courses/", views.courses),
]
