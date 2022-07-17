from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def user_login(request):

    if request.method == "POST":
        if request.POST.get('register'):
            return redirect('register')
    return render(request,'./user/login.html')


def user_register(request):
    message = ''
    form = UserCreationForm()

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        print(username, password1, password2)

        if password1 != password2:
            message = '兩次密碼不同'
        elif len(password1) < 8:
            message = '密碼過短(至少八個字)'

        else:
            # 使用者名稱是否重複
            if User.objects.filter(username=username).exists():
                message = '帳號重複'
            else:
                user = User.objects.create_user(
                    username=username, password=password1)
                if user:
                    user.save()
                    message = '註冊成功!'

    return render(request, './user/register.html', {'form': form, 'message': message})