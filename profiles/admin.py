# profiles/admin.py
from django.contrib import admin
from .models import Profile



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date')
    list_filter = ('location', 'birth_date')
    search_fields = ('user__username', 'user__email', 'bio')
    
    fieldsets = (
    ('User Information', {'fields': ('user',)}),  
    ('Profile Details', {'fields': ('bio', 'location', 'birth_date')}),
)


admin.site.register(Profile, ProfileAdmin)

