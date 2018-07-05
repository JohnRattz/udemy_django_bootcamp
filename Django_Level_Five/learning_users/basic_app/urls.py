from django.conf.urls import url
from basic_app import views as basic_app_views

# TEMPLATE URLS
app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$', basic_app_views.register, name='register')
]
