from django.shortcuts import render
from .models import News,Category
# Create your views here.
def homefn(request):
    x=News.objects.all()
    y=Category.objects.all()
    return render(request, 'home.html',{'post':x,'cat':y})
def viewfn(request,s_id):
    z=News.objects.get(id=s_id)
    return render(request, 'viewpage.html',{'s':z})
def link(request):
    return render(request,"link.html")
def catfn(request,c_id):
    x=News.objects.filter(category=c_id)
    y=Category.objects.all()
    return render(request,'category.html',{'post':x,'cat':y})