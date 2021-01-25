from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    # widoki posta
    path('', views.post_list, name='post_list'),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/', views.post_detail, name='post_detail'),
]