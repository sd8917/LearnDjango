from django.contrib import admin
from .models import Student
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class StudenAdmin(ImportExportModelAdmin):
    list_display = ('name','section','rollno','phone','topic')
    list_editable = ('phone','topic')
    search_fields = ('rollno','topic','section')
    list_filter = ('topic','section')
    list_per_page = 10

admin.site.register(Student, StudenAdmin)