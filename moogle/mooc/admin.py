from django.contrib import admin
from .models import User, Course, Lesson, Classification

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','description','mtime','ctime')
    search_fields = ('title',)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'course', 'mtime','ctime')
    search_fields = ('title',)


admin.site.register(User)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Classification)