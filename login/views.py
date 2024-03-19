from django.shortcuts import render
from baoma import email_send,vcode
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login
from .models import users
from .forms import LoginForm

# Create your views here.

"""验证表格
def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse('Authenticated'\
                                    'successfully')
"""

"""登陆视图"""
def login(request):
    result = {'code':0,'msg':'','data':''}
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    if username and password is not None:
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                result['code']=1
                result['msg']='Login successfully!'
                return JsonResponse(result,safe=False)
        else:
            result['msg']='User is not exist!'
            return JsonResponse(result,safe=False)
    else:
        result['msg']='The username or password is not entered.'
        return JsonResponse(result,safe=False)

"""邮箱发送验证码"""
def verification(request):
    emailadress = request.POST.get('email')
    result = {'code':0,'msg':'','data':''}
    global this_vcode
    this_vcode = vcode.get_vcode()
    if email_send.send_vcode(emailadress,this_vcode):
        result = {'code':1,'msg':'success!','data':'You did it!'}
    else:
        result = {'code':0,'msg':'failed~','data':'It`s a pity ~'}
    return JsonResponse(result,safe=False)


"""验证码验证注册视图"""
def registered(request):
    user_vcode = request.POST.get('vcode')
    result = {'code':0,'msg':'','data':''}
    if this_vcode == user_vcode:
        
        """obsolete
        users.username = request.POST.get('name')
        users.passsword = request.POST.get('password')
        users.email = request.POST.get('email')
        """
        
        result['code'] = 1
        users.objects.create_user(request.POST.get('email'),
                                  request.POST.get('name'),
                                  request.POST.get('password'),
                                )
            
        return JsonResponse(result,safe=False)