from django.urls import path

from main import views

urlpatterns = [
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('skills/',views.skills,name='skills'),
    path('',views.index,name='index'),

]
