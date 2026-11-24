from django.urls import path
from . import views

urlpatterns = [
    path('about/' , views.indexView , name = 'fbv-test'),
    path('post/' , views.PostListView.as_view() , name = "post=list"),
    path('cbv-index/' , views.IndexView.as_view() , name = 'cbv-index'),
    path('contact/' , views.PostCreateView.as_view() , name = "contact")

    
]