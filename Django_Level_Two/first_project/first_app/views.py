from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "Hello I'm from first_app!"}
    return render(request, 'first_app/index.html', my_dict)
