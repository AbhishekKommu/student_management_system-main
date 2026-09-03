# The main address book for the whole project.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Send everything else to our app's address book.
    path('', include('students.urls')),
]
