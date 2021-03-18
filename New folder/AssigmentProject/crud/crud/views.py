from django.shortcuts import render
from .models import crudst
from django.contrib import messages
from .forms import stform


def stdisplay(request):
    results = crudst.objects.all()
    return render(request, "index.html", {"crudst": results})


def stinsert(request):
    if request.method == "POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get(
                'staddress') and request.POST.get('stmobile') and request.POST.get('stgender'):
            savest = crudst()
            savest.stname = request.POST.get('stname')
            savest.stemail = request.POST.get('stemail')
            savest.staddress = request.POST.get('staddress')
            savest.stmobile = request.POST.get('stmobile')
            savest.stgender = request.POST.get('stgender')
            savest.status = 1
            savest.save()
            messages.success(request, "The Record " + savest.stname + " Is saved successfully..!")
            return render(request, "create.html")
    else:
        return render(request, "create.html")


def stedit(request, id):
    getstudentdetails = crudst.objects.get(id=id)
    return render(request, 'edit.html', {"crudst": getstudentdetails})


def stupdate(request, id):
    stupdate = crudst.objects.get(id=id)
    stupdate.stname = request.POST.get('stname')
    stupdate.stemail = request.POST.get('stemail')
    stupdate.staddress = request.POST.get('staddress')
    stupdate.stmobile = request.POST.get('stmobile')
    stupdate.stgender = request.POST.get('stgender')

    if stupdate.save():
        messages.success(request, "The Student Record Is Updated Successfully..!")
        return render(request, "edit.html", {"crudst": stupdate})

    else:
        messages.error(request, "Something went wrong")
        results = crudst.objects.all()
        return render(request, "index.html", {"crudst": results})
    form = stform(request.POST, instance=stupdate)
    if form.is_valid():
        form.save()
        messages.success(request, "The Student Record Is Updated Successfully..!")
        return render(request, "edit.html", {"crudst": stupdate})
    else:
        messages.error(request, "Something went wrong")
        results = crudst.objects.all()
        return render(request, "index.html", {"crudst": results})


def stdel(request, id):
    delstudent = crudst.objects.get(id=id)
    delstudent.status = 0
    delstudent.save()
    results = crudst.objects.all()
    return render(request, "index.html", {"crudst": results})


def stdeletedRecord(request):
    results = crudst.objects.all()
    return render(request, "deletedRecord.html", {"crudst": results})


def stretrive(request, id):
    delstudent = crudst.objects.get(id=id)
    delstudent.status = 1
    delstudent.save()
    results = crudst.objects.all()
    return render(request, "index.html", {"crudst": results})
