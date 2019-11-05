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


## Blog
* In this section we create the Blog with ckeditor packege

*Installation of Package
```
  pip install django-ckeditor
  $ ./manage.py collectstatic
  
```
[static file setting](https://docs.djangoproject.com/en/2.2/howto/static-files/)

* url.py(main project)
```
  path('ckeditor/', include('ckeditor_uploader.urls')),
  
```

* setting.py
```
* add following in your INSTALLED_APP
    'ckeditor',
    'ckeditor_uploader',
    
* new configuration
    CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
    CKEDITOR_UPLOAD_PATH = "/media/uploads/"
    CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media/uploads/')
    CKEDITOR_IMAGE_BACKEND = "pillow"

    CKEDITOR_CONFIGS = {
       'default': {
            'toolbar': 'full',
       },
    }

    CKEDITOR_JQUERY_URL = '/static/js/jquery-2.1.1.min.js'

```

* models.py
```
    from ckeditor.fields import RichTextField
    from ckeditor_uploader.fields import RichTextUploadingField
    
    content = RichTextField()    
```

*. How to create the slug field
```
    Slug = models.SlugField(max_length=200, unique=True) # Note the caps of the Slug
```

*. How to pass data to urls.py
```
    path('blog/<slug:slug>/',views.blogdetail,name='detail'),
```

*. How to pass data to views.py
'''
    def blogdetail(request, slug):
        post = get_object_or_404(Blog, Slug = slug)
        return render(request,'blog/blogdetail.html', {'blog':post})
'''

*. How to pass In templates
```
  <a href="{% url 'blog:detail' slug=blog.Slug %}">
  # Note here the blog is the loop iterator 
  
```
# Note
* While Using the ckeditor use the | safe
``` 
   {{ blog.content|truncatechars:200 |safe}}

```

# Accountapp

* In this we work the management of the account

### Templates structure

>templates/app_name/account.html

>templates/registration/regitster.html

>templates/registration/login.html

### urls.py of main project
'''

path('accounts/',include('django.contrib.auth.urls')),
    
path('register/',include('accountapp.urls'))
    
'''
### url.py of the app

'''

path('',views.view_name,name="view_name),

path('register',views.register,name='register')

'''

### views.py
'''

def register(request):
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form .cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username, password = password)
            #Check for login status with your database data.
            login(request, user)
            return redirect('myaccount')
            
    else:
        form = UserCreationForm()

    context = {'form' : form}

    return render(request, 'registration/register.html', context)

'''
