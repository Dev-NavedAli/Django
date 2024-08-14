from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('service/',views.service),
    path('course/',views.course),
    path('course/<courseid>',views.courseDetail),
    path('userform/',views.userform),
    path('submitform/',views.submitform,name="submitform"),
    path('calculator/',views.calculator),
    path('marksheet/',views.marksheet),
    path('detailPage/<slug>',views.detailPage),
    path('contact/',views.contact),
    path('saveenquiry',views.saveenquiry, name='saveenquiry')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)