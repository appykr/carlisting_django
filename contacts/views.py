from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(requests):
    if requests.method == 'POST':
        car_id = requests.POST['car_id']
        car_title = requests.POST['car_title']
        user_id = requests.POST['user_id']
        first_name = requests.POST['first_name']
        last_name = requests.POST['last_name']
        subject = requests.POST['customer_need']
        user_city = requests.POST['city']
        user_state = requests.POST['state']
        user_email = requests.POST['email']
        phone_number = requests.POST['phone']
        message = requests.POST['message']

        if requests.user.is_authenticated:
            user_id = requests.user.id
            has_contacted = Contact.objects.all().filter(car_id = car_id, user_id = user_id)

            if has_contacted:
                messages.error(requests, 'You have already made an inquiry. Please wait untill we get back to you')
                return redirect('/cars/'+car_id)
        contact = Contact(car_id = car_id, car_title = car_title, user_id = user_id, first_name = first_name, last_name = last_name, subject = subject, 
                          user_city = user_city, user_state = user_state, email_id = user_email, phone_number = phone_number, message = message)
        #Sending EMail
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Inquiry",
            "You have the new Inquiry for the car" + car_title + '.Please Login to your dashboard for more info',
             "arpitcoolguy1@gmail.com",
            [admin_email],
            fail_silently=False,
            )
        

        contact.save()
        messages.success(requests, "Your request has been submitted, we wil get back to you shortly.")
        


    return redirect('/cars/'+car_id)