from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import RegisterUserForm, advisorUserForm
from Tracking.models import Student, Advisor, SportsClubs, Achivement
from django.contrib.auth.hashers import make_password
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:        
            # Redirect to a success page.
            login(request, user)
            return redirect('index1')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error that have occured please try again"))
            return redirect('login')
    else:      
        return render(request, 'authenticate/login.html', {})   
    

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logout"))
    return redirect('index')


def register_user(request):
    form = RegisterUserForm()
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create a user object but don't save it yet
            user.set_password(form.cleaned_data['password1'])  # Hash the password
            
            # Capture and save additional data
            user.save()  # Save the user object with the hashed password
            
            # Create a Student object with the additional data
            student = Student(
                studentId=form.cleaned_data['studentId'],
                studentName=form.cleaned_data['studentName'],
                studentPhone=form.cleaned_data['studentPhone'],
                studentCourse=form.cleaned_data['studentCourse'],
                studentEmail=form.cleaned_data['studentEmail'],
                studentAddress=form.cleaned_data['studentAddress'],
                user=user
            )
            student.save()  # Save the student object
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('index1')
    
    return render(request, 'authenticate/register_user.html', {'form': form})


#advisor Registration

def advisor_registration(request):
    form = advisorUserForm()

    if request.method == "POST":
        form = advisorUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create a user object but don't save it yet
            user.set_password(form.cleaned_data['password1'])  # Hash the password

            user.save()
        advisor = Advisor(
        # Get data from the form
        advisorId =form.cleaned_data['advisorId'],
        advisorName =form.cleaned_data['advisorName'],
        advisorEmail =form.cleaned_data['advisorEmail'],
        advisorPhone =form.cleaned_data['advisorPhone'],
        )
        advisor.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        # Redirect to the advisor page after registration
        messages.success(request, "Registration Successful!")
        return redirect('index2')

    return render(request, 'authenticate/advisorRegister.html', {'form': form})

#advisor Login

def advisor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the user's dashboard or home page
            return redirect('index2')  # Example: redirect to the student page
        else:
            # Return an 'invalid login' error message.
            messages.error(request, ("There was an error that have occured please try again"))
            return redirect('advisorLogin')

    return render(request, 'authenticate/advisorLogin.html', {})

# Advisor Logout
def advisor_logout(request):
    logout(request)
    messages.success(request, ("You were logout"))
    return redirect('index')


#admin Login

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the user's dashboard or home page
            return redirect('index3')  # Example: redirect to the student page
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error that have occured please try again"))
            return redirect('adminLogin')

    return render(request, 'authenticate/adminLogin.html')


# Advisor Logout
def admin_logout(request):
    logout(request)
    messages.success(request, ("You were logout"))
    return redirect('index')