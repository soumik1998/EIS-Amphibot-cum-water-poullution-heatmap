from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import turbidity

from django.views import View

# Create your views here.
def index(request):
    turb = turbidity.objects.all()
    context={'turb':turb}
    return render(request,'pollution/index.html',context)


def getdata(request):
    tur_value = request.GET['turbidity_value']
    obj = turbidity()
    obj.turbidity_value = tur_value
    obj.time=datetime.now()
    obj.save()
    print('Data was sent successfully')
    return HttpResponse('This is get request')
