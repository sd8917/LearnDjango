# LearnDjango

## Importapp
* In this we are just making the use of the Import export module on Student Model
>$ pip install django-import-export

* admin.py
```
* from import_export.admin import ImportExportModelAdmin 

*         list_display = ('name','section','rollno','phone','topic')
*         list_editable = ('phone','topic')
*         search_fields = ('rollno','topic','section')
*         list_filter = ('topic','section')
*         list_per_page = 10
```
