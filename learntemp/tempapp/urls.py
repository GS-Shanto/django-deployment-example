from django.conf.urls import url
from tempapp import views

app_name='tempapp'
urlpatterns = [
url(r'^relative/$',views.relative,name='relative'),
url(r'^other/$',views.other,name='other'),

]
