from django.shortcuts import render, HttpResponse , redirect ,get_object_or_404 
from datetime import datetime
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from Rojgar.models import user_request
from django.views.generic import ListView
import uuid
from .utils import *
from Rojgar.models import user_request
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.core.mail import EmailMessage
from Rojgar.models import WorkerStat
# Create your views here.



def login_page(request):
    if request.method == "POST":
        user_name = request.POST.get("username")
        pass1 = request.POST.get("password")
        user=authenticate(request,username=user_name,password=pass1)
        if user is not None :
            login(request,user)
            return redirect('/home/')
        else:
            messages.warning(request, "Username or Password is wrong")
    return render(request , 'login-signup.html')
    
def singup_page(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        email = request.POST.get("emailAddress")
        password = request.POST.get("password")
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists. Please choose a different username.")
        else:
            # If the username is unique, create and save the user
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            messages.success(request, "You have successfully created an account.")
    return render(request , 'signup-login.html')

def home_page(request):
    hello = User.objects.all()
    print(hello.filter(username="admin"))
    if request.user.is_authenticated:
        user = request.user
        user_requests = user_request.objects.filter(email=user.email)
        return render(request,'apphome.html',{'user_requests': user_requests})
    return redirect('/login/')

def logout_page(request):
    logout(request)
    return redirect("/home")



def request(request):
     if request.user.is_authenticated:
        user_email = request.user.email
        user_name = request.user.username
        work_areas = WorkerStat.WORK_AREAS
        disctricts = [
        'Achham', 'Arghakhanchi', 'Baglung', 'Baitadi', 'Bajhang', 'Bajura',
        'Banke', 'Bara', 'Bardiya', 'Bhaktapur', 'Bhojpur', 'Chitwan', 'Dadeldhura',
        'Dailekh', 'Dang', 'Darchula', 'Dhading', 'Dhankuta', 'Dhanusa', 'Dholkha',
        'Dolpa', 'Doti', 'Eastern Rukum', 'Gorkha', 'Gulmi', 'Humla', 'Ilam', 'Jajarkot',
        'Jhapa', 'Jumla', 'Kailali', 'Kalikot', 'Kanchanpur', 'Kapilvastu', 'Kaski',
        'Kathmandu', 'Kavrepalanchok', 'Khotang', 'Lalitpur', 'Lamjung', 'Mahottari',
        'Makwanpur', 'Manang', 'Morang', 'Mugu', 'Mustang', 'Myagdi', 'Nawalparasi East',
        'Nawalparasi West', 'Nuwakot', 'Okhaldhunga', 'Palpa', 'Panchthar', 'Parbat',
        'Parsa', 'Pyuthan', 'Ramechhap', 'Rasuwa', 'Rautahat', 'Rolpa', 'Rupandehi',
        'Salyan', 'Sankhuwasabha', 'Saptari', 'Sarlahi', 'Sindhuli', 'Sindhupalchok',
        'Siraha', 'Solukhumbu', 'Sunsari', 'Surkhet', 'Syangja', 'Tanahu', 'Taplejung',
        'Terhathum', 'Udayapur', 'Western Rukum',
    ]
        
        return render(request , 'request.html',{'user_email': user_email , 'user_username': user_name, 'work_areas': work_areas ,'disctricts': disctricts,})
def formadded(request):
      if request.user.is_authenticated:
        user_email = request.user.email
        if request.method=="POST":
            name=request.user.username
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            district = request.POST.get('district')
            user_email1 = user_email
            email=user_email1
            problem=request.POST.get('problem')
            selected=request.POST.get('selected')
            Requests=user_request(name=name,phone=phone,address=address, email=email ,problem=problem , selected=selected ,date=datetime.today(),district=district)
            Requests.save()
        return render(request , 'formadded.html')
def admin_redirect(request):
    return redirect("/rojgar-superuser/")
def home_redirect(request):
    return redirect("home/")

def verify(request,token):
    try:
        obj = Profile.objects.get( email_token=token)
        obj.is_verified = True
        obj.save()
        return HttpResponse("Your email address has been verified")
    except Exception as e:
        return HttpResponse("Invalid Token")
    return True

def is_worker(user):
    return user.groups.filter(name='Worker').exists()

@user_passes_test(is_worker, login_url='/home/')
def work(request):
    # Get all requests where is_accepted is False and order by date
    data = user_request.objects.filter(is_accepted=False).order_by('date')
    worker_email = request.user.email
    worker_stat_instance = WorkerStat.objects.get(email=worker_email)
    work_area = worker_stat_instance.workarea
    worker_disctrict_real = worker_stat_instance.worker_district
    print (worker_disctrict_real)
    print(work_area)
    # data = data.filter(selected = work_area district = worker_disctrict_real)
    data= data.filter(selected = work_area , district = worker_disctrict_real)
    return render(request, 'work.html', {'data': data})
def item_detail(request, item_id):

    item = get_object_or_404(user_request, id=item_id)
    if item.is_accepted:
        
        if item.accepted_by == request.user:
            return render(request, 'item_detail.html', {'item': item})
        else:
            return HttpResponse('Request already accepted.')
    if request.method=="POST":
        service_request = user_request.objects.get(pk=item_id)
        service_request.accepted_by = request.user
        service_request.is_accepted = True
        service_request.accepted_date = datetime.today()
        service_request.save()
    return render(request, 'item_detail.html', {'item': item})

def be_worker(request):
    work_areas = WorkerStat.WORK_AREAS
    useremail = request.user.email
    disctricts = [
        'Achham', 'Arghakhanchi', 'Baglung', 'Baitadi', 'Bajhang', 'Bajura',
        'Banke', 'Bara', 'Bardiya', 'Bhaktapur', 'Bhojpur', 'Chitwan', 'Dadeldhura',
        'Dailekh', 'Dang', 'Darchula', 'Dhading', 'Dhankuta', 'Dhanusa', 'Dholkha',
        'Dolpa', 'Doti', 'Eastern Rukum', 'Gorkha', 'Gulmi', 'Humla', 'Ilam', 'Jajarkot',
        'Jhapa', 'Jumla', 'Kailali', 'Kalikot', 'Kanchanpur', 'Kapilvastu', 'Kaski',
        'Kathmandu', 'Kavrepalanchok', 'Khotang', 'Lalitpur', 'Lamjung', 'Mahottari',
        'Makwanpur', 'Manang', 'Morang', 'Mugu', 'Mustang', 'Myagdi', 'Nawalparasi East',
        'Nawalparasi West', 'Nuwakot', 'Okhaldhunga', 'Palpa', 'Panchthar', 'Parbat',
        'Parsa', 'Pyuthan', 'Ramechhap', 'Rasuwa', 'Rautahat', 'Rolpa', 'Rupandehi',
        'Salyan', 'Sankhuwasabha', 'Saptari', 'Sarlahi', 'Sindhuli', 'Sindhupalchok',
        'Siraha', 'Solukhumbu', 'Sunsari', 'Surkhet', 'Syangja', 'Tanahu', 'Taplejung',
        'Terhathum', 'Udayapur', 'Western Rukum',
    ]
    if request.method =="POST":
        email = request.user.email
        workarea = request.POST.get('workarea')
        print(workarea)
        father_name = request.POST.get('fatherName')
        grand_father_name = request.POST.get('grandfatherName')
        temporary_address = request.POST.get('temporaryAddress')
        permanent_address = request.POST.get('permanentAddress')
        citizenship_image_front = request.FILES.get('citizenshipFront')
        citizenship_image_back = request.FILES.get('citizenshipBack')
        worker_district = request.POST.get('disctrict')
        baka = WorkerStat.objects.create(email=email , workarea=workarea , father_name=father_name,grand_father_name=grand_father_name,temporary_address=temporary_address,permanent_address=permanent_address,citizenship_image_front=citizenship_image_front,citizenship_image_back=citizenship_image_back,worker_district=worker_district)
        baka.save()
        return HttpResponse('You will be called soon')

    # Other context variables can be added here if needed

    return render(request, 'beworker.html', {'work_areas': work_areas ,'useremail' :useremail, 'disctricts': disctricts,})
@login_required
def get_user_profile(request):
    user = request.user

    # Customize the data you want to include in the profile
    profile_data = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        # Add more fields as needed
    }

    return JsonResponse(profile_data)

from django.shortcuts import render, get_object_or_404
from .models import user_request, UserData, WorkerStat

from django.http import Http404

def request_detail_accepted(request, request_id):
    try:
        # Get the user request object
        request_obj = get_object_or_404(user_request, pk=request_id)

        # Check if the request is accepted
        if request_obj.is_accepted:
            # Get the UserData and WorkerStat objects for the accepted user
            accepted_user = get_object_or_404(User, username=request_obj.accepted_by.username)
            worker_stat =  get_object_or_404(WorkerStat, email=accepted_user.email)
            


            # Render the template with the request details and accepted user details
            return render(request, 'request_detail_accepted.html', {'request_obj': request_obj, 'accepted_user': accepted_user, 'worker_stat':worker_stat})
        else:
            # If the request is not accepted, render a different template or handle it accordingly
            return render(request, 'request_not_accepted.html', {'request_obj': request_obj})
    except Http404:
        # Handle the case where the user_request object is not found
        return render(request, '404.html')  # You can customize this template or redirect as needed


def request_detail_waiting(request, request_id):
    request_obj = get_object_or_404(user_request, pk=request_id)

    return render(request, 'request_detail_waiting.html', {'request_obj': request_obj})

@require_POST
def mark_work_done(request, request_id):
    # Get the request object
    request_object = get_object_or_404(user_request, id=request_id)

    # Mark the work as done
    request_object.work_done = True
    request_object.save()

    # Redirect to the same page or a different page
    return redirect('payment')
@login_required
def payment(request):
    return render(request,'payment.html')
def profile(request):
    return render(request,'profile.html')


def home(request):
    if request.user.is_authenticated:
       return redirect('/home')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        objects = ContactForm(name=name,email=email,subject=subject,message=message)
        objects.save()
        messages.success(request, "Your form has been submitted successfully")
   
    return render(request,"index.html")
