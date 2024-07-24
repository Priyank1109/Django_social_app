from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from  django.contrib.auth.hashers import check_password,make_password
import json
from django.core.files.storage import FileSystemStorage
from .models import *
# Create your views here.

@csrf_exempt
def index(request):
    response = {}
    if request.method == "POST":
        if 'uname' not in request.POST or request.POST['uname'] == "" :
            messages.error(request, "User Name is missing")
        if 'psw' not in request.POST or request.POST['psw'] == "" :
            messages.error(request, "Password is missing")
        
        uname = request.POST['uname']
        password = request.POST['psw']
        if Up_UsersDetails.objects.filter(UserName=uname).exists() :
            users = Up_UsersDetails.objects.get(UserName=uname)
            if users.password:
                # if check_password(request.POST['psw'], users.password):
                if request.POST['psw'] == users.password:
                    messages.error(request, "Logged in successfully")
                    return redirect('/lists/')
                else:
                    messages.error(request, "Invalid Credentials")
            else:
                messages.error(request, "Invalid Credentials")
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['psw']
        password_repeat = request.POST['psw-repeat']
        profile_image = request.FILES.get('image') 

        if password != password_repeat:
            messages.error(request, "Passwords do not match.")
            return redirect('register')  # Redirect back to registration form with error message
        
        # Check if email already exists
        if Up_UsersDetails.objects.filter(official_email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')
        
        if profile_image:
            storage = FileSystemStorage()
            store_image = storage.save(profile_image.name, profile_image)
            store_image_url = storage.url(store_image)
        else:
            store_image_url = None
        
        new_user = Up_UsersDetails(
            UserName=username,
            official_email=email,
            primary_contact_number=phone_number,
            password=password, # make_password(password)
            profile_image=store_image_url  # Save the image URL in the model field
        )
        new_user.save()
        messages.success(request, 'Registration successful. Please login.')
        return redirect('/login/')  # Redirect to login page after successful registration
    
    return render(request, 'register.html')


def lists(request):
    context = {}
    context['users'] = Up_UsersDetails.objects.all()
    return render(request,'list.html',context)


def update_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        user = Up_UsersDetails.objects.get(pk=user_id)
        profile_image = request.FILES.get('profile_image')
        user.UserName = request.POST.get('UserName')
        user.official_email = request.POST.get('official_email')
        user.primary_contact_number = request.POST.get('primary_contact_number')
        if request.FILES.get('profile_image'):
            storage = FileSystemStorage()
            store_image = storage.save(profile_image.name, profile_image)
            store_image_url = storage.url(store_image)
            user.profile_image = store_image_url
        else:
            store_image_url = None
            user.profile_image = store_image_url
        user.save()
        return JsonResponse({'message': 'User updated successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def delete_user(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        try:
            user = Up_UsersDetails.objects.get(pk=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully.'})
        except Up_UsersDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)