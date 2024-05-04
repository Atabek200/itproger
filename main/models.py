from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    technique = models.CharField(max_length=50)
    malfunction = models.TextField(max_length=200)
    service_time = models.DateTimeField('Дата публикации')
    documentation = models.FileField(upload_to='documents/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.technique


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)


class Request(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_master = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    datetime = models.DateTimeField('Дата публикации')


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)


class WorkOrder(models.Model):
    STATUS_CHOICES = [
        ('В процессе', 'В процессе'),
        ('Выполнено', 'Выполнено'),
        ('Отложено', 'Отложено'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='В процессе')
    datetime = models.DateTimeField('Дата Выполнина')


class NotificationForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)


class Applicationforms(models.Model):
    Name = models.CharField(max_length=100)


class Master(models.Model):
    Name = models.CharField(max_length=100)


