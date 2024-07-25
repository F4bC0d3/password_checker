from django.shortcuts import render
from .forms import PasswordStrengthForm, PasswordGeneratorForm
from .models import PasswordCheck, GeneratedPassword
import random
import string
import re

def password_strength_checker(password):
    length = len(password)
    if length < 6:
        return "Weak"
    if re.search(r"\d", password) and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\W", password):
        return "Strong"
    return "Moderate"

def check_password(request):
    if request.method == 'POST':
        form = PasswordStrengthForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            strength = password_strength_checker(password)
            PasswordCheck.objects.create(password=password, strength=strength)
            return render(request, 'checker/check_password.html', {'form': form, 'strength': strength})
    else:
        form = PasswordStrengthForm()
    return render(request, 'checker/check_password.html', {'form': form})

def generate_password(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            include_numbers = form.cleaned_data['include_numbers']
            include_special = form.cleaned_data['include_special']
            
            characters = string.ascii_letters
            if include_numbers:
                characters += string.digits
            if include_special:
                characters += string.punctuation
                
            password = ''.join(random.choice(characters) for i in range(length))
            GeneratedPassword.objects.create(
                password=password, length=length, 
                include_numbers=include_numbers, include_special=include_special
            )
            return render(request, 'checker/generate_password.html', {'form': form, 'password': password})
    else:
        form = PasswordGeneratorForm()
    return render(request, 'checker/generate_password.html', {'form': form})
