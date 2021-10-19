from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
# Built-in Tags
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


#custom-Tags
def operation(request):
    num1, num2 =1,1
    if request.method=='POST':
        num1=int(request.POST.get('inpt1'))
        num2=int(request.POST.get('inpt2'))
    context={
        'num1':num1,
        'num2':num2,
    }
    return render(request, 'custom/operation.html', context)