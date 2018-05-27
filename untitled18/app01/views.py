from django.shortcuts import render,redirect
# Create your views here.
def login(request):
    """
    登录函数
    :return:
    """

    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == '超级英雄' and password == '123':
            return redirect('/index', {'msg': name})
    elif request.method == "GET":
        return render(request, 'login.html')