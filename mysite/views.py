from django.shortcuts import render


def MASTER(request):
    return render(request,'master.html')


def INDEX(request):
    return render(request,'index.html')