from django.shortcuts import render

def index(request):
    cont_dict ={'text':'hello world','number':1000}
    return render(request,'files/index.html',cont_dict)
def other(request):
    return render(request,'files/other.html')
def relative(request):
    return render(request,'files/relative_url.html')
