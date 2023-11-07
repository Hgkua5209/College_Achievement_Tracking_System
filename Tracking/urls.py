from django.urls import path
from . import views

  
urlpatterns = [
    path('',views.index, name="index"),
    path('index1',views.index1, name="index1"),
    path('studentView', views.studentView, name ="StudentView"),
    path('studentMerit', views.studentMerit, name ="StudentMerit"),
    path('studentRequest', views.studentRequest, name ="StudentRequest"),
    path('index2',views.index2, name="index2"),
    path('AdvisorAchievement', views.advisorAchievementPost, name ="AdvisorAchievement"),
    path('AdvisorCertificate', views.advisorCertificate, name ="AdvisorCertificate"),
    path('index3',views.index3, name="index3"),
    path('adminStudent', views.adminStudent, name ="adminStudent"),
    path('adminAdvisor', views.adminAdvisor, name ="adminAdvisor"),
    path("studentUpdate/<str:studentId>",views.studentUpdate,name='studentUpdate'),
    path("studentUpdate/studentUpdatedata/<studentId>",views.studentUpdatedata,name='studentUpdatedata'),
    path('deleteStudent/<studentId>', views.deleteStudent, name='deleteStudent'),
    path("advisorUpdate/<str:advisorId>",views.advisorUpdate,name='advisorUpdate'),
    path("advisorUpdate/advisorUpdatedata/<advisorId>",views.advisorUpdatedata,name='advisorUpdatedata'),
    path('deleteAdvisor/<advisorId>', views.deleteAdvisor, name='deleteAdvisor'),
    path('submit_merit_request', views.submit_merit_request, name='submit_merit_request'),
    path('review_merit_requests', views.review_merit_requests, name='review_merit_requests'),
    path('delete_merit_request/<int:pk>/', views.delete_merit_request, name='delete_merit_request'),
    path('adminAchievementView', views.adminAchievementView, name='adminAchievementView'),
    path('adminSportClubsView', views.adminSportClubsView, name='adminSportClubsView'),
    path("adminSportCodeUpdate/<str:sportClubsCode>",views.sportCodeUpdate,name='sportCodeUpdate'),
    path("adminSportCodeUpdate/adminSportCodeUpdatedata/<sportClubsCode>",views.sportCodeUpdatedata,name='sportCodeUpdatedata'),
    path('deleteSportClubs/<sportClubsCode>', views.deleteSportClubs, name='deleteSportClubs'),
    path('deleteAchivement/<id>', views.deleteAchivement, name='deleteAchivement'),
    path('adminAcievementAdd', views.adminAcievementAdd, name ="adminAcievementAdd"),
    path('adminSportCodeAdd', views.adminSportCodeAdd, name ="adminSportCodeAdd"),
    
]

'''
    path('AdvisorAchievement', views.advisorAchievement, name ="AdvisorAchievement")
'''