from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import usersForms

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

def submitform(request):
    return HttpResponse(request)


def aboutus(request):
    return render(request,"aboutus.html")
def service(request):
    return render(request,"service.html")
def course(request):
    return HttpResponse("<b> Hi am course and this is cource page </b>")

def courseDetail(request,courseid):
    return HttpResponse(courseid)

def userform(request):
    fn = usersForms()
    try:
        # n=request.GET['name']
        # n2=request.GET['class']
        n=request.POST.get('name')
        n2=request.POST.get('class')
        print(n,n2)
        data = n,n2
        # url = '/aboutus/?output={}'.format(data)
        # return HttpResponseRedirect("/aboutus/")
    except:
        pass
    return render(request,"userform.html",{'output':data,'form':fn})


def calculator(request):
    c=''
    try:
        if request.method == "POST":
            num1 =eval( request.POST.get("num1"))
            num2 =eval(request.POST.get("num2")) 
            opr = request.POST.get("opr")
            if opr == "+":
               c=num1+num2
            elif opr == "-":
               c= num1-num2
            elif opr == "*":
               c=num1*num2
            elif opr == "/":
               c=num1/num2
    except:
        c="Invalid choice"
    print(c)
    return render(request,"calculator.html",{'c':c})