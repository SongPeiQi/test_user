from django.shortcuts import render,redirect
# Create your views here.
def login(request):
    """
    登录函数
    :return:
    """
    user_name = '超级英雄'


    return render(request,'login.html',{'msg': user_name})