from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    my_dict = {'help_text': "HELP PAGE"}
    return render(request, 'AppTwo/help.html', my_dict)

def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request) # Redirect to the index page.
        else:
            print('Error: Form Invalid')
    return render(request, 'AppTwo/users.html', {'form':form})
