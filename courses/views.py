from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

data = {
    "programming": "Programming",
    "webdevelopment": "Web Development",
    "mobileapps": "Mobile Apps",
}

def index(request):
    category_list = list(data.keys())

    return render(request, "courses/index.html", {
        "categories": category_list
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
