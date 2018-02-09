from django.conf.urls import url
from appTwo import views

app_name = 'appTwo'
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^users/',views.users,name="users"),
    url(r'^users_list',views.users_list,name="users_list")
]
