from django.shortcuts import render, redirect
from apps.buildings.models import Building, Otklic
from apps.settings.models import Settings
from django.core.mail import send_mail
# Create your views here.
def building_detail(request,id):
    setting = Settings.objects.latest('id')
    building = Building.objects.get(id = id)
    context = {
        'setting' : setting,
        'building' : building,
    }
    return render (request, 'page-project-detail-2.html', context)

def building_index(request):
    setting = Settings.objects.latest('id')
    buildings = Building.objects.all()
    context = {
        'setting' : setting,
        'buildings' : buildings,
    }
    return render (request, 'page-portfolio-grid.html', context)

def response(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        otklic = Otklic.objects.create(full_name = name, email = email, phone = phone, subject = subject, text = message)
        otklic.save()
        send_mail(
            #subject 
            f"Спасибо за отклик: {subject}", 
            #message 
            f"Здравствуйте {name}, спасибо за отклик мы с вами свяжемся. Ваше сообщение {message}, ваш номер {phone}", 
            #from email 
            'jamankulova.ayana283@gmail.com', 
            #to email 
            [email] 
        )
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render (request, 'page-contact.html', context)
    
