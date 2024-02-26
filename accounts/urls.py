from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('login/', views.login_view, name='account_login'),
    path('signup/', views.signup_view, name='account_signup'),
    # other URL patterns
]
