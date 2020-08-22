from django.shortcuts import render,redirect
from .models import RegisterData,ContactData
from .forms import  RegisterForm,LoginForm,ContactForm,PasswordForm
from django.http import HttpResponse

def regview(request):
    if request.method == 'POST':
        rform = RegisterForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name', '')
            gender = rform.cleaned_data.get('gender', '')
            username = request.POST.get('username', '')
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            mobile = request.POST.get('mobile', '')
            dob = rform.cleaned_data.get('dob', '')

            data = RegisterData(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                username=username,
                password1=password1,
                password2=password2,
                email=email,
                mobile=mobile,
                dob=dob
            )
            data.save()
            rform = RegisterForm()
            lform = LoginForm()
            return render(request, 'reg.html', {'rform':rform, 'lform': lform})
        if request.method == 'POST':
            lform = LoginForm(request.POST)
            if lform.is_valid():
                username = request.POST.get('username','')
                password1 = request.POST.get('password1','')

                user = RegisterData.objects.filter(username=username)
                pwd = RegisterData.objects.filter(password1=password1)

                if user and pwd:
                    return redirect('/home/')
                else:
                    return HttpResponse('Invalid credentials')
        # lform = LoginForm()
        # return render(request,'reg.html',{'lform':lform})
    else:
        rform = RegisterForm()
        lform = LoginForm()
        return render(request,'reg.html',{'rform':rform ,'lform':lform})

# def loginview(request):
#     if request.method == 'POST':
#         lform = LoginForm(request.POST)
#         if lform.is_valid():
#             username = request.POST.get('username','')
#             password1 = request.POST.get('password1','')
#
#             user = RegisterData.objects.filter(username=username)
#             pwd = RegisterData.objects.filter(password1=password1)
#
#             if not user and pwd:
#                 return HttpResponse('Invalid')
#             else:
#                 return redirect('/home/')
#     else:
#         lform = LoginForm()
#         return render(request,'login.html',{'lform':lform})

def home(request):
    return render(request,'matrimony_home.html')


def boys(request):
    bData = RegisterData.objects.filter(gender='male')
    return render(request,'boys.html',{'bData':bData})


def gilrs(request):
    gData = RegisterData.objects.filter(gender='female')
    return render(request, 'girls.html', {'gData': gData})


def service(request):
    return render(request, 'matrimony_service.html')


def contact(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name = request.POST.get('name','')
            gender = cform.cleaned_data.get('gender','')
            email = request.POST.get('email','')
            mobile = request.POST.get('mobile','')
            about = request.POST.get('about','')
        data = ContactData(
                name = name,
                gender = gender,
                email = email,
                mobile = mobile,
                about = about
            )
        data.save()
        cform = ContactForm()
        return render(request,'matrimony_contact.html', {'cform':cform})
    else:
        cform = ContactForm(request.POST)
        return render(request,'matrimony_contact.html',{'cform':cform})


def gallery(request):
    return render(request, 'matrimony_gallery.html')


def forgotpassword(request):
    if request.method == 'POST':
        pform = PasswordForm(request.POST)
        if pform.is_valid():
            uname1 = pform.cleaned_data.get('username')
            pass1 = pform.cleaned_data.get('password1')
            pass2 = pform.cleaned_data.get('password2')

            try:
                x=RegisterData.objects.filter(username = uname1)
                if pass1 == pass2:
                    x.update(password1 = pass1)
                    x.update(password2 = pass2)
                    return redirect('/#/')
                else:
                    return HttpResponse("Password mismatch")

            except RegisterData.DoesNotExist:
                return HttpResponse("User not found")
        else:
            return HttpResponse("Invalid form")
    else:
        pform = PasswordForm()
        return render(request,'institute_forgotpass.html',{'pform':pform})


def logout(request):
    return redirect('/#/')


def user(request):
    uData = RegisterData.objects.all()
    return render(request,'user.html',{'uData':uData})