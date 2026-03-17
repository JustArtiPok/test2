from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Advertisement(models.Model):
    class Status(models.TextChoices):
        OPEN = 'OPEN', 'Открыто'
        CLOSED = 'CLOSED', 'Закрыто'
        # DRAFT = 'DRAFT', 'Черновик'  # для доп. задания

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.OPEN,
        verbose_name='Статус'
    )
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='advertisements',
        verbose_name='Автор'
    )
    
    # Для доп. задания - избранное
    favorited_by = models.ManyToManyField(
        User, 
        related_name='favorite_advertisements',
        blank=True,
        verbose_name='Добавили в избранное'
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title