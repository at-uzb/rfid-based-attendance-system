from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Attendance)
admin.site.register(Room)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #list_display = ['name', 'surname']
    list_filter = ['group']
    search_fields = ['name', 'surname','group']

