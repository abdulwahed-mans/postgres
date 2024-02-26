# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views
from products import views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', include('pages.urls')),
    path('products/', include('products.urls')),
    #path('profile/edit/', views.profile_edit, name='profile_edit'),
    #path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
    # path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    # path('profile/', include(('profiles.urls', 'profiles'), namespace='profiles')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
