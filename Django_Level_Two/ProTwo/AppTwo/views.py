from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    print("help")
    my_dict = {'help_text': "HELP PAGE"}
    return render(request, 'AppTwo/help.html', my_dict)

def users(request):
    print("users")
    users = User.objects.order_by('first_name')
    users_dict = {'users': users}
    return render(request, 'AppTwo/users.html', users_dict)
