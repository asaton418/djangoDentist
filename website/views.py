from django.shortcuts import render
from django.core.mail import send_mail
import environ

env = environ.Env()
env.read_env('.env')

def home(request):
    return render(request, 'home.html', {})

def contact(request):     
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = "Contact request : " + request.POST['message-subject']
        message = request.POST['message']
        send_email=env('HOSTEMAIL')

        # send an email 
        send_mail(
            message_subject, # subject
            message, # message
            message_email, # from email
            [send_email], # To Email
            )

        return render(request, 'contact.html', {'message_name': message_name})
    
    else:
        return render(request, 'contact.html', {})

def about(request):
        return render(request, 'about.html', {})

def service(request):
        return render(request, 'service.html', {})

def appointment(request):
        return render(request, 'appointment.html', {})

def appointment2(request):
    if request.method == "POST":
        your_service = request.POST['your-service']
        your_doctor = request.POST['your-doctor']
        your_name = request.POST['your-name'] 
        your_email = request.POST['your-email'] 
        your_date = request.POST['your-date']
        your_time = request.POST['your-time'] 
        send_email=env('HOSTEMAIL')
        
        print('Your service: %s Your doctor: %s Your name: %s Your email: %s Your date: %s Your time: %s' 
        % (your_service, your_doctor, your_name, your_email, your_date, your_time)      
        )

        appointment= "Name:" + your_name + " Service: " + your_service + " Doctor:" + your_doctor + " Date: " + your_date + " Time: " + your_time        
        # send an email 
        send_mail(
            "Appointment Request", # subject
            appointment, # message
            your_email, # from email
            [send_email], # To Email
            )

        return render(request, 'appointment2.html', {
                'your_service': your_service,
                'your_doctor': your_doctor,
                'your_name': your_name,
                'your_email': your_email,
                'your_date': your_date,
                'your_time': your_time, })
    
    else:
        return render(request, 'home.html', {})


def price(request):
        return render(request, 'price.html', {})

def team(request):
        return render(request, 'team.html', {})

def testimonial(request):
        return render(request, 'testimonial.html', {})