from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages 
import smtplib 
import random
import logging
from django.utils import timezone
from urllib.parse import quote

logger = logging.getLogger(__name__)


email_ = "djangotest027@gmail.com"
password_ = "ndvx oxnp kftb tslg"

def home(request):
   context = {'page':'Home'}
   return render(request, 'index.html', context)

def about(request):
   context = {'page':'About'}
   return render(request, 'about.html', context)

def reg_page(request):   

   global mail_
   global password_ 
   

   if request.method == "POST":
      data = request.POST

      user_name = data.get('user_name')
      ph_number = data.get('ph_number')
      password = data.get('password')
      email = data.get('email')
      otp_number = random.randint(1000,9999)

      try:
            otp_record=Ontimepassword.objects.create(
                user_name=user_name,
                otp_number=otp_number,
                ph_number=ph_number,
                password=password,
                email=email,
            )
            
      except Exception as e:
          return (str(e))
     
           
      try:
            sender = email_
            receiver = email

           #subject = "Registration Successful"
            subject = "OTP for registration"
            body = f"""
            Hello {user_name},

            Your otp is {otp_number}

            Best regards,
            Nikhil
            """

            # Email message formatting
            email_text = f"Subject: {subject}\n\n{body}"

            gmail_user = email_
            gmail_app_password = password_
            sent_from = email_
            sent_to = email
            

            try:
                  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                  server.ehlo()
                  server. login(gmail_user, gmail_app_password)
                  server.sendmail(sent_from, sent_to, email_text)
                  server.close()

                  print("Email sent!")
            
            
            except Exception as exception:
                  print(str(exception))

            otp_record_id = otp_record.id
            encoded_otp_record_id = quote(str(otp_record_id))

            return redirect(f'/otp_page/?otp_record_id={encoded_otp_record_id}')
            
      except Exception as e:
        print(str(e))



   context = {'page':'Regstration'}
   return render(request, 'reg_page.html', context)

def otp_page(request):   

   global mail_
   global password_ 
   

   if request.method == "POST":
      data = request.POST
      otp_record_id = request.GET.get('otp_record_id')

      otp_user = data.get('otp_user')
      logger.info(f"Received OTP: {otp_user}, ")
      

      try:
            
            otp_record = Ontimepassword.objects.get(id=otp_record_id)
            email=otp_record.email
            user_name=otp_record.user_name
            logger.info(f"OTP record found for user: , OTP: {otp_record.otp_number}")
      except Ontimepassword.DoesNotExist:
            messages.error(request, "OTP record not found. Please try registering again.")
            return redirect('/error_page/')
     
      if otp_record.otp_number == int(otp_user):    
            try:
                Registration.objects.create(
                    user_name=otp_record.user_name,
                    ph_number=otp_record.ph_number,
                    password=otp_record.password,
                    email=otp_record.email,
                )
                 
            
            except Exception as exception:
                messages.error(request, f"Error saving data: {str(exception)}")
            try:
                  sender = email_
                  receiver = email

                  #subject = "Registration Successful"
                  subject = " registration"
                  body = f"""
                  Hello {user_name},

                  Registered

                  Best regards,
                  Nikhil
                  """

                  # Email message formatting
                  email_text = f"Subject: {subject}\n\n{body}"

                  gmail_user = email_
                  gmail_app_password = password_
                  sent_from = email_
                  sent_to = email
                  

                  try:
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server. login(gmail_user, gmail_app_password)
                        server.sendmail(sent_from, sent_to, email_text)
                        server.close()

                        print("Email sent!")
                  
                  
                  except Exception as exception:
                        print(str(exception))

            except Exception as e:
                  return (e)

            
            otp_record.delete()      
                
            
            return render(request, 'success_page.html')         
      else:
          return render(request, 'error_page.html')
      
  
   otp_record_id = request.GET.get('otp_record_id')


   context = {'page':'OTP page','otp_record_id': otp_record_id}
   return render(request, 'otp_page.html', context)


def success_page(request):
   context = {'page':'Success'}
   return render(request, 'success_page.html',context)

def error_page(request):
   context = {'page':'Error'}
   return render(request, 'error_page.html',context)

def info_page(request):
   data = Registration.objects.all()

   stu = {
      "user_name" : data
   }


   context = { 'user_name' : 'user_name',
         'ph_number' : 'ph_number',
         'password' : 'password',
         'email' : 'email',
      }
   sui = {'page':'Infopage'}
   return render(request, 'infopage.html', stu )



