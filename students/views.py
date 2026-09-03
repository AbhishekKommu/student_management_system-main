# A view is a Python function.
# It takes a request and returns a response.

from django.shortcuts import render


def home(request):
    # This list is fake data for now. On Day 2 it comes from the database.
    course_names = [
        'Database Management Systems',
        'Operating Systems',
        'Web Technologies',
        'Computer Networks',
        'Software Engineering',
    ]

    # render() needs 3 things: the request, the template name, and the data.
    return render(request, 'students/home.html', {'courses': course_names})


def about(request):
    return render(request, 'students/about.html')


def contact(request):
    return render(request, 'students/contact.html')
