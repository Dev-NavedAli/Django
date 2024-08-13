from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import usersForms
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contactenquiry.models import contactEnquiry



def home(request):
    newsData = News.objects.all()
    #iconatains ka kaam hota hai ki ek letter se bhi data search ho jaaye 
    serviceData = Service.objects.all()
    paginator= Paginator(serviceData,2)
    page_number = request.GET.get('page')
    serviceDataFinal = paginator.get_page(page_number)
    totalpage = serviceDataFinal.paginator.num_pages

    if request.method == 'GET':
        st = request.GET.get('inputsearch')
        if st!=None:
            serviceData = Service.objects.filter(service_title__icontains=st)
    data = {
        'serviceData':serviceDataFinal,
        'lastpage':totalpage,
        'pageList':[i+1 for i in range(totalpage) ],
        'newsData':newsData
    }
    return render(request,"index.html",data)

def submitform(request):
    return HttpResponse(request)


def detailPage(request,slug):
    newsdetail = News.objects.get(news_slug = slug)
    data ={
        'newsdetail':newsdetail
    }
    return render(request,"detailPage.html",data)

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

def contact(request):
    return render(request,"contact.html")

def saveenquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        manage = request.POST.get('manage')
        en = contactEnquiry(name=name,email=email,phone=phone,website_name=website,manage=manage)
        en.save()


    return render(request,"contact.html")

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

def marksheet(request):
    total = ""
    percentage=""
    grade=""
    try:
        if request.method == "POST":
            # if request.POST.get("Subject1") == "":    for bootstrap error agar field khai hone pr 5:18:01 pr wscube ki vdo
            #     return render(request,"marksheet.html",{'error':True})
            Subject1 = eval(request.POST.get("Subject1"))
            Subject2 = eval(request.POST.get("Subject2"))
            Subject3 = eval(request.POST.get("Subject3"))
            Subject4 = eval(request.POST.get("Subject4"))
            Subject5 = eval(request.POST.get("Subject2"))
            total=Subject1+Subject2+Subject3+Subject4+Subject5
            percentage= total/500*100
            percentage = round(percentage,2)
            if percentage >80:
                grade  = "Grade A+"
            elif percentage > 60 and percentage<80:
                grade = "Grade b"
            elif percentage > 40 and percentage < 60:
                grade = "Grade c"
            else:
                grade  = "Fail" 
    except:
        total ="Invalid choice"
        
    print(total)
    
    return render(request,"marksheet.html",{'total':total,'percentage':percentage,'grade':grade})