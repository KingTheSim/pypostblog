from django.urls import path
from .views import user_registration, staff_user_registration, super_user_registration


urlpatterns = [
    path('registration/user_registration', user_registration, name="user_registration"),
    path('registration/staff_user_registration', staff_user_registration, name="staff_user_registration"),
    path('registration/super_user_registration', super_user_registration, name="super_user_registration"),
]