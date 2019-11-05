from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

    # import the form for user creation
from django.contrib.auth.forms import UserCreationForm

# for checking of authentication we should import authenticate and login for login

from django.contrib.auth import authenticate, login

# Create your views here.
def myaccount(request):
    return render(request, 'accountapp/account.html')

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
