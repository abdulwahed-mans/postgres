# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from profiles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include('pages.urls')),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    # path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    # path('profile/', include(('profiles.urls', 'profiles'), namespace='profiles')),
]
