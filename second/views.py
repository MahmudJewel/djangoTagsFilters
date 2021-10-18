from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def string(request):
    txt=''
    if request.method=='POST':
        #if request.POST.get('lower'):
        txt=request.POST.get('tarea')
            #print(txt)
    context={
            'txt':txt,
        }
    return render(request,'BuiltInTags/string.html', context)
    
def reference(request):
    return render(request,'BuiltInTags/Reference.html')
