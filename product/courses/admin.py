from django.contrib import admin

from courses.models import Course, Lesson, Group

admin.site.register(Course)
admin.site.register(Lesson)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', )
