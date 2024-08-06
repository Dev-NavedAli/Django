from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    data = {
        'tittle':'Home Page',
        'bdata':'Welcome to real world',
        'cdata':["Python","mern","java"],
        'numbers':[10,20,30,40,50,60,70],
        'student_details':[
            {'name':'jijo','phone':8054682324},
            {'name':'kiko','phone':8054546832}
        ]
    }
    return render(request,"index.html",data)

def aboutus(request):
    return render(request,"aboutus.html")
def course(request):
    return HttpResponse("<b> Hi am course and this is cource page </b>")

def courseDetail(request,courseid):
    return HttpResponse(courseid)