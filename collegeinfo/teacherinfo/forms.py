from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    department = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned = super().clean()

        # Password check
        if cleaned.get("password") != cleaned.get("confirm_password"):
            raise forms.ValidationError("Passwords do not match.")

        # Phone validation
        phone = cleaned.get("phone")
        if phone and len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")

        return cleaned
