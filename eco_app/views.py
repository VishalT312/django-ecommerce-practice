from django.shortcuts import render, HttpResponse, redirect
from eco_app.models import Contact, Product
from django.contrib import messages


# ()
# Create your views here.


def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # we can also do like this-> request.POST.get('name)
            name = request.POST['name']
            email = request.POST['email']
            pnumber = request.POST['pnumber']
            desc = request.POST['desc']
            myquery = Contact(name=name, email=email,
                              phonenumber=pnumber, desc=desc)
            myquery.save()
            messages.info(request, 'we will get back to you soon')
            # return render(request, 'contact.html')

        return render(request, 'contact.html')
    else:
        messages.info(request, 'for contact you have to login first')
        return redirect('/auth/login/')


def about(request):
    return render(request, 'about.html')
