from django.shortcuts import render , redirect
from django.http import HttpResponse
from reg.models import *
from django.contrib import messages
from urllib.parse import quote


def login(request):
   if request.method == "POST":
        data = request.POST

        user_name = data.get('user_name')
        password = data.get('password')

        try:
            
            accinfo = Registration.objects.get(user_name=user_name)

            
            if password == accinfo.password:
                 user_id = accinfo.id
                 encoded_user_id = quote(str(user_id))
                 return redirect(f'/dashboard/?user_id={encoded_user_id}')

      
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

   context = {'page': 'Login Page'}
   return render(request, 'login.html', context)
            
    
def dashboard(request):
   user_id = request.GET.get('user_id')
   context={'page':'dashboard'}
   return render(request, 'dashboard.html',context)

def accinfo(request):
    if request.method == "POST":
        data = request.POST

        user_name = data.get('user_name')
        password = data.get('password')

        try:
            
            accinfo = Registration.objects.get(user_name=user_name)

            
            if password == accinfo.password:
                
                context = {
                    'user_name': accinfo.user_name,
                    'ph_number': accinfo.ph_number,
                    'email': accinfo.email,
                    'password': accinfo.password,
                    'page': 'Account Information'
                }


                return render(request, 'accinfo.html', context)
            
            else:
                messages.error(request, "Invalid password. Please try again.")

              
        except Registration.DoesNotExist:
            messages.error(request, "User not found. Please check your credentials.")
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            
            
    
    context = {'page': 'Account Information'}
    return render(request, 'accinfo.html', context)

def preupdateinfo(request):
    if request.method == "POST":
        data = request.POST

        user_name = data.get('user_name')
        password = data.get('password')

        try:
            
            accinfo = Registration.objects.get(user_name=user_name)

            
            if password == accinfo.password:
                 user_id = accinfo.id
                 encoded_user_id = quote(str(user_id))
                 return redirect(f'/updateinfo/?user_id={encoded_user_id}')

      
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

    context = {'page': 'Confirmation'}
    return render(request, 'preupdateinfo.html', context)


def updateinfo(request):
    user_id = request.GET.get('user_id')
    
    if request.method == "POST":
      data = request.POST

      new_user_name = data.get('new_user_name')
      new_ph_number = data.get('new_ph_number')
      new_password = data.get('new_password')
      new_email = data.get('new_email')

      try:
            
            accinfo = Registration.objects.get(id=user_id)
            accinfo.user_name = new_user_name
            accinfo.ph_number = new_ph_number
            accinfo.password = new_password
            accinfo.email = new_email

            accinfo.save()

            return render(request, 'infopage.html')

      except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")

      
    context = {'page': 'Update Information'}
    return render(request, 'updateinfo.html', context)
      





