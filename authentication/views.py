import threading

from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, logout, login
from .models import CustomUser
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import genrate_token
from django.core.mail import EmailMessage
from django.conf import settings


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


# Create your views here.

def login_user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            if request.user.is_email_verified:
                return redirect('profile1')
        return render(request, 'authentication_templates/signin.html')
    if request.method == "POST":
        context = {'data': request.POST}

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            if not user.is_email_verified:
                messages.add_message(request, messages.ERROR, "Email is not verified")
                return render(request, 'authentication_templates/signin.html', context)
            else:
                login(request, user)
                print(request.user.username)
                return redirect('profile1')
        if not user:
            messages.success(request, "Bunday foydalanauvchi topilmadi. Qaytadan urinib ko'ring!")
            return redirect('profile1')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        user = authenticate(request, username=username, password=password1)

        if user is None:
            myuser = CustomUser.objects.create_user(username, email, password1)
            send_activation_email(request, user=myuser)
            messages.success(request, "Siz tizimdan royxatdan o'tdingiz Tizimga kirish uchun pochtangizni tasdiqlang")
            return redirect('login')
        return redirect('login')

    return render(request, 'authentication_templates/register.html')


def logout_user(request):
    logout(request)
    return redirect('')


def activate_user(request, uid64, token):
    print('sendingbiw')
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = CustomUser.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and genrate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS, "Email verified, you can now login")
        return redirect(reverse('login'))

    return render(request, 'authentication_templates/activate-failed.html',
                  {"user": user
                   })


def send_activation_email(request, user):
    current_site = get_current_site(request)
    email_subject = "Activate your account"
    email_body = render_to_string('authentication_templates/activate.html',
                                  context={'user': user,
                                           'domain': current_site,
                                           'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                           'token': genrate_token.make_token(user)
                                           })
    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_HOST_USER, to=[user.email])
    EmailThread(email).start()
