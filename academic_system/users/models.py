# Create your models here.
from django.contrib.auth.models import AbstractUser # Importa AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _ # Para internacionalización de textos

class CustomUser(AbstractUser):
    """
    Modelo de Usuario Personalizado que extiende AbstractUser de Django.
    Añade campos comunes y un tipo de usuario para roles principales.
    """
    # Define las opciones para el tipo de usuario
    USER_TYPE_CHOICES = (
        ('student', _('Estudiante')), # Estudiante
        ('faculty', _('Docente')), # Profesor/Docente
        ('admin_staff', _('Staff Facultativo')), # Personal Administrativo
        # Puedes añadir más tipos si es necesario, e.g., 'super_admin'
    )
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='student', # Valor por defecto cuando se crea un usuario
        verbose_name=_("Tipo de usuario"), # Tipo de Usuario
        help_text=_("Designar tipo de usuario") # Texto de ayuda para el campo
    )

    # Campos adicionales comunes a todos los usuarios del sistema académico
    phone_number = models.CharField(
        max_length=20,
        blank=True, # Puede estar en blanco en formularios
        null=True,   # Puede ser NULL en la base de datos
        verbose_name=_("Numero de Teléfono"),
        help_text=_("Contacto telefónico del usuario.")
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Domicilio"),
        help_text=_("Domicilio del usuario.")
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Fecha de Nacimiento"),
        help_text=_("Fecha de nacimiento del usuario.")
    )
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    # Puedes añadir más campos genéricos aquí si todos los tipos de usuario los necesitan
    # Por ejemplo:
    # national_id = models.CharField(max_length=50, unique=True, blank=True, null=True, verbose_name=_("National ID"))

    class Meta:
        """
        Clase Meta para opciones del modelo. # sirve para definir metadatos del modelo. 
        """
        verbose_name = _("User") # Nombre singular en el admin
        verbose_name_plural = _("Users") # Nombre plural en el admin
        ordering = ['first_name', 'last_name', 'username'] # Orden por defecto para consultas

    def __str__(self):
        """
        Método de representación de cadena del objeto.
        Útil para el panel de administración y depuración.
        """
        if self.first_name and self.last_name: # Si tiene nombre y apellido, devuelve el nombre completo
            return self.get_full_name() # Heredado de AbstractUser
        return self.username

    # Métodos de conveniencia para verificar el tipo de usuario
    def is_student(self): 
        return self.user_type == 'student'

    def is_faculty(self):
        return self.user_type == 'faculty'

    def is_admin_staff(self):
        return self.user_type == 'admin_staff'

    # Puedes añadir más métodos personalizados aquí
    # Por ejemplo, para obtener el rol específico si hay un modelo relacionado
    def get_specific_role_object(self): 
        if self.is_student():
            try:
                # Asumiendo que Student tiene un  OneToOneField'user' a CustomUser
                return self.student
            except AttributeError:
                return None
        elif self.is_faculty():
            try:
                # Asumiendo que Faculty tiene un OneToOneField 'user' a CustomUser
                return self.faculty
            except AttributeError:
                return None
        return None

