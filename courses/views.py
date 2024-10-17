from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from courses.forms import CourseCreateForm
from courses.models import Course, Category

def index(request):
    #list comprehension
    courses = Course.objects.all(isActive=True, isHome=True)
    category_list = Category.objects.all()

    # for course in db["courses"]:
    #     if course["isActive"]:
    #         courses.append(course)

    return render(request, "courses/index.html", {
        "categories": category_list,
        "courses": courses
    })

def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            course = Course(title = form.cleaned_data["title"],
                            description = form.cleaned_data["description"],
                            imageUrl = form.cleaned_data["imageUrl"],
                            slug = form.cleaned_data["slug"])
            course.save()
            return redirect("/courses")
    form = CourseCreateForm()
    return render(request, "courses/create_course.html", {"form":form})

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        courses = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        categories = Category.objects.all()
    else :
        return redirect("/courses")


    return render(request, "courses/search.html", {
        "categories": categories,
        "courses": courses,
        
    })



def details(request, slug):
    # try:
    #     course = Course.objects.get(pk=course_id)
    # except:
    #     raise Http404("Course not found")

    course = get_object_or_404(Course, slug=slug)
    context = {
        "course": course
    }
    return render(request, "courses/details.html", context)


def getCoursesByCategory(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    categories = Category.objects.all()

    paginator = Paginator(courses, 2)
    page = request.GET.get("page", 1)
    page_obj = paginator.page(page)

    return render(request, "courses/list.html", {
        "categories": categories,
        "page_obj": page_obj,
        "selected_category": slug
    })


