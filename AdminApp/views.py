from django.shortcuts import render

def layout(request):
    contex = {}
    return render(request,'AdminApp/layout.html',contex)

def dash(request):
    contex = {}
    return render(request,'AdminApp/dashboard.html',contex)

def common_form(request):
    contex = {}
    return render(request,'AdminApp/common_form.html',contex)

