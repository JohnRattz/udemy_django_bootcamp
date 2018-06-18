from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    # my_dict = {'insert_content': "Hello I'm from first_app!"}
    return render(request, 'first_app/index.html', date_dict)
