from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages

# Create your views here.

# ()

# :

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        if password != confirm_password:
            messages.warning(request,'Password is not matching.')
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,'Email is taken')
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password) # first one is for username but here we take it as email 
        user.is_active=False
        user.save() 
        email.subject='activate your account'
        messages=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        }) 











        return HttpResponse('user created',email)

    return render(request,'signup.html')





def handlelogin(request):
    return render(request,'login.html')

def handlelogout(request):
    return redirect('/auth/login')