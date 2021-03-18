from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import Contact


# Create your views here.
def index(request):
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
    return render(request, 'index.html')


def studentList(request):
    stud = Contact.objects.all()
    return render(request, 'studentList.html', {'stud': stud})


def updateStudent(request, id):
    return render(request, 'updateStudent.html', {id: id})


def deleteData(request, id):
    if request.method == "POST":
        stud = Contact.objects.get(pk=id)
        stud.delete()
        return HttpResponseRedirect('/')