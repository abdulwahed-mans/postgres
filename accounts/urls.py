from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='account_login'),
    path('signup/', views.signup_view, name='account_signup'),
    # other URL patterns
]
