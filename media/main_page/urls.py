from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='About Us'),
    path('t-shirts/', views.tshirt, name='T-Shirts'),
    path('trousers/', views.trouser, name='Trousers'),
    path('contact/', views.contact, name='Contact Us'),
    path('tracker/', views.tracker, name='Product current Status'),
    path('search/', views.search, name='Search'),
    path('checkout/', views.checkout, name='Checkout'),
    path("products/home-pr<int:myid>", views.productView, name="ProductView"),
    path("tshirtVeiw/tshirt-pr<int:myid>", views.tshirtView, name="tshirtView"),
    path("trouserVeiw/trousers-pr<int:myid>", views.trouserView, name="trouserView"),
    path('Order a custom design/', views.custom_design, name='Costom Design'),
    path('Apply for Job/', views.job_application, name='job_application'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
