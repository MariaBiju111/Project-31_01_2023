from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('book/',views.book),
    path('book_detail/<int:id>/',views.book_detail),

]