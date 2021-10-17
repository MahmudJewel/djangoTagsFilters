from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def lower(request):
    return render(request,'BuiltInTags/lower.html')
    
def reference(request):
    return render(request,'BuiltInTags/Reference.html')
