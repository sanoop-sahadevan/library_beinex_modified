from library import views 
from django.urls import path

# importing views from views..py


urlpatterns = [
	path('', views.HomePageView.as_view(),name="Home"),
    path("Booklist/",views.Booklist.as_view(),name="booklist"),
    
    path('Bookcreate/',views.create_blog,name="blogcreate"),
    path("authorlist/",views.Authorlist.as_view(),name="authorlist"),
    path("Bookdetails/",views.Bookdetails.as_view(),name="Bookdetails"),
    path('delete/<int:pk>/', views.delete_view,name='book_delete'),
    path('update/<int:pk>/', views.Update,name='book_update'),

	
]
