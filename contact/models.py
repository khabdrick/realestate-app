# from django.db import models

# from django.core.mail import send_mail

# from .views import Contact, Subscription, Blog



# def contact_send_mail(self):


#     html_ = [name, email, message, subject, phone_number]
#     subject = subject
#     from_email = 'MJ Realtor <laceyduvalle01@gmail.com>'
#     recipient_list = ['jacecorporation1@gmail.com']
#     sent_mail = send_mail(
#                 subject,
#                 txt_,
#                 from_email,
#                 recipient_list,
#                 html_message=html_,
#                 fail_silently=False,

#         )
#     return sent_mail



# def subscribe_send_mail(self):

#     html_ = semail
#     subject = "Subscription"
#     from_email = 'MJ Realtor <laceyduvalle01@gmail.com>'
#     recipient_list = ['jacecorporation1@gmail.com']
#     sent_mail = send_mail(
#                 subject,
#                 txt_,
#                 from_email,
#                 recipient_list,
#                 html_message=html_,
#                 fail_silently=False,

#         )
#     return sent_mail


# def blog_send_mail(self):

#     html_ = bemail
#     subject = "Blog"
#     from_email = 'MJ Realtor <laceyduvalle01@gmail.com>'
#     recipient_list = ['jacecorporation1@gmail.com']
#     sent_mail = send_mail(
#                 subject,
#                 txt_,
#                 from_email,
#                 recipient_list,
#                 html_message=html_,
#                 fail_silently=False,

#         )
#     return sent_mail


# # class ContactUs(models.Model):
# # 	name 				= models.CharField(max_length=50)
# # 	email				= models.EmailField(max_length=50)
# # 	subject				= models.CharField(max_length=50, blank=True, null=True)
# # 	message				= models.TextField(max_length=500)
# # 	phone_number		= models.IntegerField(blank=True, null=True)
# # 	timestamp			= models.DateTimeField(auto_now_add=True)


# # 	def __str__(self):
# # 		return self.subject


# # class Subscription(models.Model):
# # 	email 				= models.EmailField(max_length=50)
# # 	timestamp			= models.DateTimeField(auto_now_add=True)

# # 	def __str__(self):
# # 		return self.email

# # class BlogEmail(models.Model):
# # 	email 				= models.EmailField(max_length=50)
# # 	timestamp			= models.DateTimeField(auto_now_add=True)

# # 	def __str__(self):
# # 		return self.email