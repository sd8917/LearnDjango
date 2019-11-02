from django.shortcuts import render,redirect
from .import form
from .form import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template

# Create your views here.

def index(request):

    Contact_Form = ContactForm
    if request.method == "POST":
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact.email')
            contact_content = request.POST.get('content')

            template = get_template('myapp/contact_form.txt')

            context = {
                'content_name' : contact_name,
                'content_email' : contact_email,
                'contact_content': contact_content,
            }
            content = template.render(context)

            email = EmailMessage(
                'New Contact form email',
                content,
                "myBlogger" + '',
                ['sudhanshuraj8917@gmail.com'],
                headers={'Reply to':
                 contact_email }

            )
            email.send()

            return redirect('myapp:index')

    return render(request,'myapp/index.html',{'form':Contact_Form})