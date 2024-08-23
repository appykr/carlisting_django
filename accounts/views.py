from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(requests, user)
            messages.success(requests, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(requests, 'Invalid Login Credential')
            return redirect('login')
    return render(requests, 'accounts/login.html')

#Register view
def register(requests):
    if requests.method =='POST':
        firstname = requests.POST['firstname']
        lastname = requests.POST['lastname']
        username = requests.POST['username']
        email = requests.POST['email']
        password = requests.POST['password']
        confirm_password = requests.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(requests, 'Username already exist')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(requests, 'Email already exist!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    user.save()
                    auth.login(requests,user)
                    messages.success(requests, 'You are now logged in')
                    return redirect('dashboard')
        else:
            messages.error(requests, 'Password do not match')
            return redirect('register')
    else:
        return render(requests, 'accounts/register.html')

#Dashboard
@login_required(login_url = 'login')
def dashboard(requests):
    user_inquiry = Contact.objects.order_by('-created_date').filter(user_id=requests.user.id)
    context = {
        'inquiries': user_inquiry,
    }
    return render(requests, 'accounts/dashboard.html', context)

#logout
def logout(requests):
    if requests.method == 'POST':
        auth.logout(requests)
        messages.success(requests, 'You are successfully logged out')
        return redirect('login')
    return redirect('home')