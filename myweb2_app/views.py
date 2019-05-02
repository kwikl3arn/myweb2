from django.shortcuts import render
from myweb2_app.models import users
# Create your views here.


# logi page view
def login(request):
    if request.method == 'POST':
        uemail = request.POST['uemail']
        upass = request.POST['upass']
        if  uemail and upass is not None:
            if users.objects.filter(email=uemail, password=upass).count()>0:
                # session creation
                request.session['emp'] = 'hello'


                request.session['auth_user_id'] = "good bye"

               # session retrive
                print(request.session['emp'])
                print(request.session['auth_user_id'])
                return render(request,'home.html')

            else:
                pass
        else:
            pass
    else:
        return render(request, 'login.html')


# register page view
def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        uemail = request.POST['uemail']
        upass = request.POST['upass']
        if uname and uemail and upass is not None:
            print(request.POST)
            if users.objects.filter(email=uemail). exists():
                return render(request, 'register.html', {"err":"sorrey email already exist"})
            else:
                users.objects.create(name=uname, email=uemail, password=upass)
                return render(request, 'login.html',{"success": "pls login to continue"})
        else:
            return render(request, 'register.html',{"err1": "pls fill all boxes"})
    else:
        return render(request, 'register.html')
