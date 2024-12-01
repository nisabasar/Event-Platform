from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Erkek'), ('female', 'Kadın'), ('other', 'Diğer')]
    )
    interests = models.TextField(null=True, blank=True)  # JSON formatında tutulabilir

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # related_name değiştirildi
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # related_name değiştirildi
        blank=True
    )
    
# Etkinlik Modeli
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    duration = models.DecimalField(max_digits=5, decimal_places=2)  # Saat cinsinden
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')

# Katılımcı Modeli
class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

# Mesaj Modeli
class Message(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
