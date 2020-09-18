from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

subject = ''
message = ''
from_email = ''


def send_email(request):
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    from_email = request.POST.get('email')
    if subject and message and from_email:
        send_mail(subject, message, from_email, recipient_list = ['jacecorporation1@gmail.com'])
        return redirect('home')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'page/contact.html')

    def send_activation(self):
        if not self.activated and not self.forced_expired:
            if self.key:
                base_url = getattr(settings, 'BASE_URL', 'https://www.pythonecommerce.com')
                key_path = reverse("account:email-activate", kwargs={'key': self.key}) # use reverse
                path = "{base}{path}".format(base=base_url, path=key_path)
                context = {
                    'path': path,
                    'email': self.email
                }
                txt_ = get_template("registration/emails/verify.txt").render(context)
                html_ = get_template("registration/emails/verify.html").render(context)
                subject = '1-Click Email Verification'
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [self.email]
                sent_mail = send_mail(
                            subject,
                            txt_,
                            from_email,
                            recipient_list,
                            html_message=html_,
                            fail_silently=False,

                    )
                return sent_mail
        return False