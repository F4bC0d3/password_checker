# checker/models.py
from django.db import models

class PasswordCheck(models.Model):
    password = models.CharField(max_length=100)
    strength = models.CharField(max_length=10)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.password} - {self.strength}"

class GeneratedPassword(models.Model):
    password = models.CharField(max_length=100)
    length = models.IntegerField()
    include_numbers = models.BooleanField(default=True)
    include_special = models.BooleanField(default=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.password
