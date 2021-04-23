from django.urls import path
from .import views
from django.conf.urls import url

app_name = "blog_app"

urlpatterns = [
    # path('', views.login, name="login"),
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('category/', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('post/<id>/', views.post, name="post"),
    # path('contact_data/', views.contact_data, name="contact_data"),
]