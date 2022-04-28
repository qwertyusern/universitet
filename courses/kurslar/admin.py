
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


@admin.register(Yonalish)
class StudentAdmin(ModelAdmin):
    pass

@admin.register(Ustoz)
class StudentAdmin(ModelAdmin):
    pass
@admin.register(Fan)
class StudentAdmin(ModelAdmin):
    pass

