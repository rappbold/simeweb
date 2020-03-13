from django.contrib import admin
from .models import Alumno
# admin.site.register(Alumno)
# Register your models here.
# Define the admin class


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'anhio', 'seccion', 'nivel')
    list_filter = ('anhio', 'seccion', 'nivel')

# admin.site.register(Alumno, AlumnoAdmin)
