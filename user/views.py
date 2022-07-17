from django.shortcuts import render

# Create your views here.
def user_register(reguest):
    return render(reguest,'./user/register.html')