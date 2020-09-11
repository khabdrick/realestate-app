from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject = subject, message = message, from_email= from_email, recipient_list = ['jacecorporation1@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'page/contact.html')