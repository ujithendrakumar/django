from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def about(request ):
    return render(request,'home/about.html',ls)

def test(request,name):
    ls = {'name':name}
    return render(request,'home/test.html',ls)