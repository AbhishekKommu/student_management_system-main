from django.contrib import admin
from .models import Department, Course, Student
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'hod_name', 'student_count']
    search_fields = ['code', 'name', 'hod_name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'department', 'semester', 'credits']
    list_filter = ['department', 'semester']
    search_fields = ['code', 'name']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'full_name', 'email', 'department', 'year_of_study', 'is_active']
    list_filter = ['department', 'year_of_study', 'is_active']
    search_fields = ['roll_no', 'first_name', 'last_name', 'email']

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)


    