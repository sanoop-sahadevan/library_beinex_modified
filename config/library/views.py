# from msilib.schema import ListView,TemplateView
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from library.forms import Blogform
from django.shortcuts import redirect, render
from django.urls import reverse_lazy


# from config.library.models import Book, Author
from django.views.generic import (TemplateView, ListView, DeleteView,UpdateView)
from .models import Book, Author


class HomePageView(TemplateView):
    template_name = "home.html"
    


class Booklist(ListView):
    model = Book
    template_name = "Booklist.html"
    # context_object_name = 'books'
  


class Authorlist(ListView):
    model = Author
    template_name = "authorlist.html"


class Bookdetails(TemplateView):
    model = Book
    template_name = "Bookdetails.html"


# Create your function views here.
def Home_page(request):

    return render(request, "home.html")


def create_blog(request):
    form = Blogform()
    if request.method == 'POST':
        form = Blogform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    context = {"form": form}
    return render(request, "blog_create_form.html", context)



def delete_view(request,pk):
    task=Book.objects.get(id=pk)   
    if request.method=='POST':
        task.delete()
        # messages.success(request, "Task Deleted Successfully !!!")
        # return redirect('assign')
    
    # context={'object':task}
    return redirect('booklist')



# class Update(UpdateView):  
#     model=Book
#     template_name="update.html"
#     fields = '__all__'
#     # success_url = 'Booklist.html'
#     # def get(self, request):
#     #     return redirect("booklist")
    
def Update(request,pk):
    task=Book.objects.get(id=pk)
    form= Blogform(request.POST )
    if request.method=='POST':
        form= Blogform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    context={"form":form}
    return render(request,"update.html",context=context)