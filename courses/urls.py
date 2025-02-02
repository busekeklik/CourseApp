from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("search", views.search, name="search"),
    path("create-course", views.create_course, name="create_course"),
    path("<slug:slug>", views.details, name = "course_details"),
    path("category/<slug:slug>", views.getCoursesByCategory, name="courses_by_category"),
]
