from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import  Studentmaster



def register(request):
    return  render(request,'student_registration.html')

def submitdata(request):

    if request.method == 'POST':

         sname = request.POST['sname']

         fname = request.POST['fname']

         dob = request.POST['dob']

         gender = request.POST['gender']

         address = request.POST['address']

         mno = request.POST['mno']

         s = Studentmaster(sname=-sname,fname=fname,dob=dob,gender=gender,address=address,mno=mno)

         s.save()

         print("data saved sucessfully")
         return render(request,'student_registration.html')

    else:

        return render(request,'studentdata.html')