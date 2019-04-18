from django.conf.urls import url
from . import views
app_name='modelformapp'
urlpatterns=[
    url(r'$',views.insert,name='insert'),
]