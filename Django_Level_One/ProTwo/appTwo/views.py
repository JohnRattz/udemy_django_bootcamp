from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    my_dict = {'help_text': "HELP PAGE"}
    return render(request, 'AppTwo/help.html', context=my_dict)
