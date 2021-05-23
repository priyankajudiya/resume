from django.http import request, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from . import models
from . import forms

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
#INDEX View
def index(request):
    # Models
    profile = models.profile
    edu = models.education
    skils = models.skils
    know = models.knowledge
    exp = models.experience

    portfolio = models.portfolio
    contactForm = forms.contactForm()

    user = profile.objects.get(pk=1)
    port = portfolio.objects.filter(portFor_id = user.pk)
    Edu = edu.objects.all().order_by('-eduYear')
    Skils = skils.objects.all()
    Exp = exp.objects.all()
    try:
        know = know.objects.get(knoFor_id = user.pk)
        Know = know.knowledges.split(',')
    except:
        Know =[]

    designation = user.designation.split(',')
    # print(Know)
    return render(request, 'index/index.html', {
                                                'user':user,
                                                'designation':designation,
                                                'edu':Edu,
                                                'skils':Skils,
                                                'know':Know,
                                                'exp':Exp,
                                                'port':port,
                                                'contactForm': contactForm,
                                                })
#INDEX View

#Ajex contact
class contact(View):
    def post(self, request):
        model = models.contact
        form = forms.contactForm(request.POST)
        if form.is_valid:
            name = request.POST.get('fullName')
            to_mail = request.POST.get('email')
            sub = request.POST.get('subject')
            msg = request.POST.get('message')

            subject = 'thank you for connecting with me'
            message = f'Hi {name}, i will contect ASAP'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [to_mail,]
            send_mail( subject, message, email_from, recipient_list )

            ################ mail to me
            subject = f'New message from {name}'
            message = f'''Name: {name}
            From: Web Resume 
            Subject: {sub}
            Message: {msg}
            Email: {to_mail}
            '''
            email = settings.EMAIL_HOST_USER
            recipient = ['pilu.ajudiya@gmail.com','ajudiyapriyank87@gmail.com']
            send_mail( subject, message, email, recipient )
            form.save()
            return HttpResponse('submited')
#Ajex contact

class portfolio(View):
    def get(self, request, pk):
        portfolio = models.portfolio
        port = portfolio.objects.get(pk=pk)
        tech = port.technology.split(',')
        return render(request, 'portfolio.html', {'port':port, 'tech':tech})
