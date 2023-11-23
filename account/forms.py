from django import forms
from .models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["email", "name", "password"]


class StaffUserRegistrationForm(UserRegistrationForm):
    class Meta(UserRegistrationForm.Meta):
        fields = ["email", "name", "password", "is_staff"]


class SuperUserRegistrationForm(StaffUserRegistrationForm):
    class Meta(StaffUserRegistrationForm.Meta):
        fields = ["email", "name", "password", "is_staff", "is_superuser"]
