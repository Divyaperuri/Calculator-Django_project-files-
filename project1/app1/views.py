from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def demo(request):
    solution=""
    if request.method== 'POST':
        n1=eval(request.POST.get("x"))
        n2=eval(request.POST.get("y"))
        opr=request.POST.get("opr")
        if opr=="+":
            solution=n1+n2
        elif opr=="-":
            solution=n1-n2
        elif opr=="*":
            solution=n1*n2
        elif opr=="/":
            solution=n1/n2
        elif opr=="%":
            solution=n1%n2
        elif opr=="**":
            solution=n1**n2
    return render(request,"calculator.html",{'solution':solution})