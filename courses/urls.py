from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("details", views.details),
    path("programming", views.programming),
    path("mobileapps", views.mobileapps),
    path("category/<str:category_id>", views.getCoursesByCategoryId),
    path("category/<int:category_name>", views.getCoursesByCategory, name="courses_by_category"),
]
