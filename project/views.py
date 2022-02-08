from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from .models import Upload

def index(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
         
        data ={
            
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = ''' 
        NEw message: {}
        From: {}
        '''.format(data['message'], data['email'])
        email=EmailMessage(data['subject'], message, 'sharique413@gmail.com', ['Sharique413@gmail.com'])
        file = request.FILES['docfile']
        email.attach(file.name, file.read(), file.content_type)
        email.send()
    return render(request, 'contactforms2/index.html', {})