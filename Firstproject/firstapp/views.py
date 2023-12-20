from django.shortcuts import render
from .models import Iplmatches

# Create your views here.
def home(request):
    if request.method == 'POST':
        ename = request.POST ['name']
        eHeadcoach = request.POST['Headcoach']
        ecaptain = request.POST['captain']
        eno_of_Trophies= request.POST['no_of_Trophies']  
        ipl = Iplmatches(name=ename,Headcoach=eHeadcoach,captain=ecaptain)
        ipl.save()  
    ipls = Iplmatches.objects.all()
    return render(request,'index.html',{'data':ipls})