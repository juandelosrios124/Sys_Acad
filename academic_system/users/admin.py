from django.contrib import admin

# Registra el modelo CustomUser en el panel de administración de Django
from .models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Clase para personalizar la visualización del modelo CustomUser en el panel de administración.
    """
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('username', 'first_name', 'last_name', 'email')

