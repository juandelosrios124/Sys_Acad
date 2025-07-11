from django.db import models


DAYS = [
    ('Monday', 'Lunes'),
    ('Tuesday', 'Martes'),
    ('Wednesday', 'Miércoles'),
    ('Thursday', 'Jueves'),
    ('Friday', 'Viernes'),
    ('Saturday', 'Sábado'),
    ('Sunday', 'Domingo'),
]

# Create your models here.
class Enrollment(models.Model): #esto es un modelo de inscripción
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('active', 'Activa'), ('withdrawn', 'Retirada')])

class Grade(models.Model): #esto es un modelo de calificación
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateField(auto_now_add=True)

class AcademicPeriod(models.Model):   #esto es un modelo de periodo académico
    name = models.CharField(max_length=50)  # Ej: "1er Semestre 2025"
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)

class Schedule(models.Model): #esto es un modelo de horario
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=30)

class Attendance(models.Model): #esto es un modelo de asistencia
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Presente'), ('absent', 'Ausente')])

