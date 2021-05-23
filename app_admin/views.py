from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

from app_core import models, forms
# Create your views here.

class admin(View):
    def get(self, request):
        profileModel = models.profile
        profile = profileModel.objects.get(pk=1)
        profileForm = forms.profileForm()

        return render(request, 'admin/admin.html', {"profile":profile, "pform": profileForm})

class saveProfile(View):
    def get(self,request):
        return HttpResponse('Not Allowed')
    def post(self, request, uid):
        print(uid)
        profileModel = models.profile
        profile = profileModel.objects.get(pk=uid)

        profile.name = request.POST['name']
        profile.mname = request.POST['mname']
        profile.lname = request.POST['lname']
        profile.pic = "main-photo/"+request.POST['pic']
        profile.designation = request.POST['designation']
        profile.age = request.POST['age']
        profile.country = request.POST['country']
        profile.state = request.POST['state']
        profile.city = request.POST['city']
        profile.address = request.POST['address']
        profile.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.description = request.POST['description']
        profile.save()
        return HttpResponse('Form Saved')
