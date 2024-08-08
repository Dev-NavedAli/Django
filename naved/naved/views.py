from django.http import HttpResponse , HttpResponseRedirect
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
def service(request):
    return render(request,"service.html")
def course(request):
    return HttpResponse("<b> Hi am course and this is cource page </b>")

def courseDetail(request,courseid):
    return HttpResponse(courseid)

def userform(request):
    try:
        # n=request.GET['name']
        # n2=request.GET['class']
        n=request.POST.get('name')
        n2=request.POST.get('class')
        print(n,n2)
        data = n,n2
        url = '/aboutus/?output={}'.format(data)
        # return HttpResponseRedirect("/aboutus/")
    except:
        pass
    return render(request,"userform.html",{'output':data})
    