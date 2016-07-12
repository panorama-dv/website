from django.conf.urls import url
from main import views


app_name = 'main'

urlpatterns = [
    url(r'^$', views.get_main_page, name='main'),
]