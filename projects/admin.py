from django.contrib import admin

from projects.models import *

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'start_date', 'end_date')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'department', 'contact',)
    search_fields = ('name', 'roll_no',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Mentor)
