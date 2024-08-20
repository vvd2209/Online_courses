from django.contrib import admin

from users.models import CustomUser, Balance, Subscription


admin.site.register(CustomUser)


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'bonus_points',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('course', 'student',)
