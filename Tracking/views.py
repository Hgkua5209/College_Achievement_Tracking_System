from django.shortcuts import render
from django.template import loader
from Tracking.models import Student, Advisor, SportsClubs, Achivement
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import MeritRequest
from .forms import MeritRequestForm

# Create your views here.

def index(request):
    return render (request,"Tracking/index.html")

def index1(request):
    return render (request,"Tracking/index1.html")

def index2(request):
    return render (request,"Tracking/index2.html")

def index3(request):
    return render (request,"Tracking/index3.html")

def studentView(request):
    Stud = Student.objects.all()
    dict = {
        'Stud':Stud,
    }
    return render(request,"Tracking/studentView.html",dict)

def studentMerit(request):
    # Get all achievements
    achievements = Achivement.objects.all()
    
    # Calculate the total merit
    total_merit = achievements.aggregate(total_merit=Sum('merit'))['total_merit']
    
    context = {
        'achievements': achievements,
        'total_merit': total_merit,
    }
    
    return render(request, "Tracking/studentMerit.html", context)

def studentRequest(request):
    return render (request,"Tracking/studentRequest.html")

def advisorAchievementPost(request):
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        student = Student.objects.get(studentId=studentId)
        advisorId = request.POST.get('advisorId')
        advisor = Advisor.objects.get(advisorId=advisorId)
        sportClubsCode = request.POST.get('sportClubsCode')
        sportClubs = SportsClubs.objects.get(sportClubsCode=sportClubsCode)
        session = request.POST['session']
        date = request.POST['date']
        achivement = request.POST['achivement']
        merit = request.POST['merit']
        data = Achivement(studentId=student, advisorId=advisor, sportClubsCode=sportClubs, session=session, achivement=achivement, date=date, merit=merit)
        data.save()
        dict={
            'message': 'Data Save'
        }
        return render(request, 'Tracking/AdvisorAchievement.html',dict)
    else:
        dict = {
            'message':' '
        }
        return render(request, 'Tracking/AdvisorAchievement.html',dict)
    
def advisorCertificate(request):
    return render (request,"Tracking/AdvisorCertificate.html")

def adminStudent(request):
    Stud = Student.objects.all()
    dict = {
        'Stud':Stud,
    }
    return render(request,"Tracking/adminStudent.html",dict)

def adminAdvisor(request):
    ad = Advisor.objects.all()
    dict = {
        'ad':ad,
    }
    return render(request,"Tracking/adminAdvisor.html",dict)


#update
#student
def studentUpdate(request,studentId):
    upstud = Student.objects.get(studentId=studentId)
    template = loader.get_template('Tracking/studentUpdate.html')
    context={
        'upstud':upstud
    }
    return HttpResponse(template.render(context, request))


def studentUpdatedata(request, studentId):
    studentName = request.POST['studentName']
    studentPhone = request.POST['studentPhone']
    studentAddress = request.POST['studentAddress']
    studentCourse = request.POST['studentCourse']
    studentEmail = request.POST['studentEmail']
    upstud = Student.objects.get(studentId=studentId)
    upstud.studentName=studentName
    upstud.studentPhone=studentPhone
    upstud.studentAddress=studentAddress
    upstud.studentCourse=studentCourse
    upstud.studentEmail=studentEmail
    upstud.save()
    return HttpResponseRedirect(reverse("index3"))


#advisor
def advisorUpdate(request, advisorId):
    uplect = Advisor.objects.get(advisorId=advisorId)
    template = loader.get_template('Tracking/advisorUpdate.html')
    context={
        'uplect':uplect
    }
    return HttpResponse(template.render(context, request))


def advisorUpdatedata(request, advisorId):
    advisorName = request.POST['advisorName']
    advisorPhone = request.POST['advisorPhone']
    advisorEmail = request.POST['advisorEmail']
    uplect = Advisor.objects.get(advisorId=advisorId)
    uplect.advisorName=advisorName
    uplect.advisorPhone=advisorPhone
    uplect.advisorEmail=advisorEmail
    uplect.save()
    return HttpResponseRedirect(reverse("index3"))

#SportCode
def sportCodeUpdate(request, sportClubsCode):
    upSC = SportsClubs.objects.get(sportClubsCode=sportClubsCode)
    template = loader.get_template('Tracking/adminSportCodeUpdate.html')
    context={
        'upSC':upSC
    }
    return HttpResponse(template.render(context, request))

def sportCodeUpdatedata(request, sportClubsCode):
    sportClubsName = request.POST['sportClubsName']
    sportClubsDescription = request.POST['sportClubsDescription']
    upSC = SportsClubs.objects.get(sportClubsCode=sportClubsCode)
    upSC.sportClubsName=sportClubsName
    upSC.sportClubsDescription=sportClubsDescription
    upSC.save()
    return HttpResponseRedirect(reverse("index3"))

#delete

#student
def deleteStudent(request, studentId):
  upstud = Student.objects.get(studentId=studentId)
  upstud.delete()
  return HttpResponseRedirect(reverse('index3'))

#advisor
def deleteAdvisor(request, advisorId):
  uplec = Advisor.objects.get(advisorId=advisorId)
  uplec.delete()
  return HttpResponseRedirect(reverse('index3'))

#SportClubs
def deleteSportClubs(request, sportClubsCode):
  uplec = SportsClubs.objects.get(sportClubsCode=sportClubsCode)
  uplec.delete()
  return HttpResponseRedirect(reverse('index3'))

#Achievement
def deleteAchivement(request, id):
  achievements = Achivement.objects.get(id=id)
  achievements.delete()
  return HttpResponseRedirect(reverse('index3'))



# views.py

def submit_merit_request(request):
    if request.method == 'POST':
        form = MeritRequestForm(request.POST, request.FILES)
        if form.is_valid():
            merit_request = form.save()
            # You can also set additional data like the user who submitted the request
            # merit_request.user = request.user  # If using Django's built-in user authentication
            merit_request.save()
            return redirect('index1')  # Redirect to a success page
    else:
        form = MeritRequestForm()

    return render(request, 'Tracking/submit_merit_request.html', {'form': form})

def review_merit_requests(request):
    merit_requests = MeritRequest.objects.filter(status=False)  # Fetch unreviewed requests
    return render(request, 'Tracking/review_merit_requests.html', {'merit_requests': merit_requests})

def delete_merit_request(request, pk):
    merit_request = MeritRequest.objects.get(pk=pk)
    merit_request.delete()
    return redirect('review_merit_requests')



def adminAchievementView(request):
    # Get all achievements
    achievements = Achivement.objects.all()
    
    # Calculate the total merit
    total_merit = achievements.aggregate(total_merit=Sum('merit'))['total_merit']
    
    context = {
        'achievements': achievements,
        'total_merit': total_merit,
    }
    
    return render(request, "Tracking/adminAchievementView.html", context)

def adminSportClubsView(request):
    SC = SportsClubs.objects.all()
    dict = {
        'SC':SC,
    }
    return render(request,"Tracking/adminSportClubsView.html",dict)

def adminAcievementAdd(request):
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        student = Student.objects.get(studentId=studentId)
        advisorId = request.POST.get('advisorId')
        advisor = Advisor.objects.get(advisorId=advisorId)
        sportClubsCode = request.POST.get('sportClubsCode')
        sportClubs = SportsClubs.objects.get(sportClubsCode=sportClubsCode)
        session = request.POST['session']
        date = request.POST['date']
        achivement = request.POST['achivement']
        merit = request.POST['merit']
        data = Achivement(studentId=student, advisorId=advisor, sportClubsCode=sportClubs, session=session, achivement=achivement, date=date, merit=merit)
        data.save()
        dict={
            'message': 'Data Save'
        }
        return render(request, 'Tracking/adminAcievementAdd.html',dict)
    else:
        dict = {
            'message':' '
        }
        return render(request, 'Tracking/adminAcievementAdd.html',dict)
    

#post adminSportCodeAdd
def adminSportCodeAdd(request):
    if request.method == 'POST':
        sportClubsCode = request.POST['sportClubsCode']
        sportClubsName = request.POST['sportClubsName']
        sportClubsDescription = request.POST['sportClubsDescription']
        data = SportsClubs(sportClubsCode=sportClubsCode, sportClubsName=sportClubsName, sportClubsDescription=sportClubsDescription)
        data.save()
        dict={
            'message': 'Data Save'
        }
        return render(request, 'Tracking/adminSportCodeAdd.html',dict)
    else:
        dict = {
            'message':' '
        }
        return render(request, 'Tracking/adminSportCodeAdd.html',dict)