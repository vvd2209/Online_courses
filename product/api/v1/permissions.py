from django.db.models import F
from rest_framework import status
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response

from users.models import Subscription
from courses.models import Group


def make_payment(request, course):
    if request.user.balance.bonus_points >= course.price:
        request.user.balance.bonus_points = F("bonus_points") - course.price
        request.user.balance.save()
        request.user.balance.refresh_from_db()

        return Response({'message': 'Оплата прошла успешно!'}, status=status.HTTP_201_CREATED)
    else:
        raise ValueError("Недостаточно бонусных баллов для оплаты курса.")


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return Subscription.objects.filter(
            student=request.user, course__id=view.kwargs.get("course_id")
        ).exists()

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return Subscription.objects.filter(
            student=request.user, course__lessons=obj
        ).exists()


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
