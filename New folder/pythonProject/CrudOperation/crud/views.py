from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import Contact
from .forms import stform


# Create your views here.
def studentForm(request):
    if request.method == "POST":
        usn = request.POST.get('usn', '')
        name = request.POST.get('name', '')
        semester = request.POST.get('semester', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        if usn and name and semester and email:
            contact = Contact(usn=usn, name=name, semester=semester, phone=phone, email=email)
            contact.save()
        else:
            return HttpResponse("enter all the details")
    return render(request, 'studentList.html')


def studentList(request):
    stud = Contact.objects.get(status="1")
    return render(request, 'studentList.html', {'stud': stud})


def editStudent(request, id):
    studentDetails = Contact.objects.get(id=id)
    return render(request, 'editDetails.html', {"studentDetails": studentDetails})


def updateStudent(request, id):
    studentDetails = Contact.objects.get(id=id)
    usn = request.POST.get('usn', '')
    name = request.POST.get('name', '')
    semester = request.POST.get('semester', '')
    phone = request.POST.get('phone', '')
    email = request.POST.get('email', '')
    details = studentDetails(usn=usn, name=name, semester=semester, phone=phone, email=email)
    details.save()
    return HttpResponseRedirect('/')


def deleteData(request, id):
    if request.method == "POST":
        stud = Contact.objects.get(id=id)
        stud(status="0")
        stud.save()
        return HttpResponseRedirect('/')