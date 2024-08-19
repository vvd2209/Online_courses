from django.contrib import admin

from users.models import CustomUser, Balance, Subscription


admin.site.register(CustomUser)


@admin.register(Balance)
class UserAdmin(admin.ModelAdmin):
    list_display = ('student', 'bonus_points',)


@admin.register(Subscription)
class UserAdmin(admin.ModelAdmin):
    list_display = ('course', 'student',)
