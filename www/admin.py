# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Person # Se importa modelo para que se "vea" dentro del admin

# Register your models here.

# Se registra modelo para que se vea en el admin
admin.site.register(Person)
