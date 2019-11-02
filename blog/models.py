from django.db import models
#Importing your Richtext file here
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Blog (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    content = RichTextField() # Note this RichTextField model provided by Ckeditor
    tag = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)

#This method used name the Blog object name 
    def __str__(self):
        return self.title
        
#This is used to determine the order of the blog a/c to Date
    class Meta:
        ordering = ('-date',)
    
