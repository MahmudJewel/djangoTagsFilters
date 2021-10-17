from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def lower(request):
    txt=''
    if request.method=='POST':
        txt=request.POST.get('tarea')
        #print(txt)
    context={
            'txt':txt,
        }
    return render(request,'BuiltInTags/lower.html', context)
    
def reference(request):
    return render(request,'BuiltInTags/Reference.html')
