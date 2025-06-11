from django.contrib import admin
from .models import (
    Enrollment,
    Grade,
    AcademicPeriod,
    Schedule,
    Attendance
)

# ---
# Clases ModelAdmin para personalizar el panel de administración
# ---

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Enrollment en el panel de administración.
    """
    # Muestra estos campos en la lista de registros de Enrollment
    list_display = ('student', 'course', 'enrollment_date', 'status')
    # Permite filtrar por estos campos
    list_filter = ('status', 'enrollment_date')
    # Permite buscar por estos campos
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
    # Convierte los campos ForeignKey en campos de entrada de ID en lugar de selectores grandes
    # Esto es útil para muchos registros.
    raw_id_fields = ('student', 'course')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Grade en el panel de administración.
    """
    list_display = ('enrollment', 'value', 'date_recorded')
    list_filter = ('date_recorded',)
    search_fields = ('enrollment__student__first_name', 'enrollment__course__name', 'value')
    raw_id_fields = ('enrollment',)

@admin.register(AcademicPeriod)
class AcademicPeriodAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo AcademicPeriod en el panel de administración.
    """
    list_display = ('name', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('name',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Schedule en el panel de administración.
    """
    list_display = ('course', 'day', 'start_time', 'end_time', 'classroom')
    list_filter = ('day', 'classroom', 'course')
    search_fields = ('course__name', 'classroom')
    raw_id_fields = ('course',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Personaliza la visualización del modelo Attendance en el panel de administración.
    """
    list_display = ('enrollment', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('enrollment__student__first_name', 'enrollment__course__name')
    raw_id_fields = ('enrollment',)
    


    