from django.conf.urls import url
from bobross_jr import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^birthday$', views.birthday, name="birthday"),
]
