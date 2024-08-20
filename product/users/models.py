from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="balance", verbose_name="Студент")
    bonus_points = models.PositiveBigIntegerField(default=1000, verbose_name="Бонусы")

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="subscriptions",
                               verbose_name="Курс")
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="subscriptions",
                                verbose_name="Студент")

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

    def pay(self) -> None:
        if self.student.balance.bonus_points < self.course.price:
            raise ValidationError("У Вас недостаточно средств.")
