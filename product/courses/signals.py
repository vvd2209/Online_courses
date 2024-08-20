from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from users.models import Subscription
from courses.models import Group


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.
    """

    if created:
        groups = Group.objects.filter(course=instance.course)

        # Если группы не созданы, создаём их
        if not groups.exists():
            for i in range(1, 11):  # создаём 10 групп
                Group.objects.create(course=instance.course, title=i)

            groups = Group.objects.filter(course=instance.course)

        # Находим самую менее заполненную группу
        least_populated_group = min(groups, key=lambda g: g.students.count())

        # Добавляем студента в выбранную группу
        least_populated_group.students.add(instance.student)
