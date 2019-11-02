from django.contrib import admin

from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    #add list display property with these three field
    list_display = ('title', 'tag', 'date')
   #add list filter property in the left of the left
    list_filter = ('tag','date')

admin.site.register(Blog, BlogAdmin)
