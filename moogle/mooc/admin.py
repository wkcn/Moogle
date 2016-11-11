from django.contrib import admin
from .models import User, Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','description','mtime','ctime')
    search_fields = ('title',)

admin.site.register(User)
admin.site.register(Course, CourseAdmin)