from django.shortcuts import render , get_object_or_404 , redirect
from .models import Apps, Service , Message , BlueTick_info , ads_banner
from django.urls import reverse


# Create your views here.

def index_view(request):
    app = Apps.objects.all().order_by('-show')
    service = Service.objects.all()

    ads = ads_banner.objects.all()

    return render(request , 'main_app/index.html' , context={'app' : app , 'service' : service , 'ads' : ads })

def App_details_view(request , slug):
    App = get_object_or_404(Apps, slug=slug)
    return render(request , "main_app/card_page.html" , context={'app' : App})


def Service_details_view(request , slug):
    service = get_object_or_404(Service, slug=slug)

    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        phone = request.POST.get('phone')
        Message.objects.create(phone=phone , full_name=full_name , service=service)
        return redirect(reverse('index'))


    return render(request , "main_app/form_page.html" , context={'service' : service})
