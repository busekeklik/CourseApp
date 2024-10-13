from datetime import date, datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

data = {
    "programming": "Programming",
    "webdevelopment": "Web Development",
    "mobileapps": "Mobile Apps",
}

db = {
    "courses": [
        {
            "title": "Python Programming",
            "description": "Learn Python Programming",
            "category": "programming",
            "image_url":" ",
            "slug": "python-programming",
            "date":datetime.now(),
            "isActive": True,
            "isUpdated": False
        },
        {
            "title": "Django Web Development",
            "description": "Learn Django Web Development",
            "category": "webdevelopment",
            "image_url":" ",
            "slug": "django-web-development",
            "date":date(2021, 1, 2),
            "isActive": False,
            "isUpdated": True
        },
        {
            "title": "Flask Web Development",
            "description": "Learn Flask Web Development",
            "category": "webdevelopment",
            "image_url":" ",
            "slug": "flask-web-development",
            "date":date(2021, 1, 3),
            "isActive": True,
            "isUpdated": True
        }
    ],
    "categories": [ 
        {"id": 1, "name" : "programming", "slug": "programming"}, 
        {"id": 2, "name" : "webdevelopment", "slug": "webdevelopment"}, 
        {"id": 3, "name" : "mobileapps", "slug": "mobileapps"}
    ]
}

def index(request):
    #list comprehension
    courses = [course for course in db["courses"] if course["isActive"]]
    category_list = db["categories"]

    # for course in db["courses"]:
    #     if course["isActive"]:
    #         courses.append(course)

    return render(request, "courses/index.html", {
        "categories": category_list,
        "courses": courses
    })

def details(request):
    return HttpResponse("Hello, Details!")

def programming(request):
    return HttpResponse("Hello, Programming!")

def mobileapps(request):
    return HttpResponse("Hello, Mobile Apps!")

def getCoursesByCategory(request, category_name):
    try:
        category_text = data[category_name];
        return render(request, "courses/category.html", {
            "category": category_name,
            "category_text": category_text})
    except:
        return HttpResponseNotFound("Category not found")

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if category_id < 1 or category_id > len(category_list):
        return HttpResponseNotFound("Category not found")
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category", args=[category_name])

    return redirect(redirect_url)
