from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, unique=True)

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает исполнителя'),
        ('in_progress', 'В процессе'),
        ('completed', 'Выполнена')
    ]

    client = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, limit_choices_to={'is_client': True})
    employee = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_employee': True})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    report = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if self.status == 'completed' and not self.report:
            raise ValueError('Отчет не может быть пустым при закрытии задачи.')
        super().save(*args, **kwargs)
