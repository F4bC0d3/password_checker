# checker/admin.py
from django.contrib import admin
from .models import PasswordCheck, GeneratedPassword

@admin.register(PasswordCheck)
class PasswordCheckAdmin(admin.ModelAdmin):
    list_display = ('password', 'strength', 'checked_at')
    search_fields = ('password', 'strength')
    list_filter = ('strength', 'checked_at')

@admin.register(GeneratedPassword)
class GeneratedPasswordAdmin(admin.ModelAdmin):
    list_display = ('password', 'length', 'include_numbers', 'include_special', 'generated_at')
    search_fields = ('password',)
    list_filter = ('include_numbers', 'include_special', 'generated_at')
