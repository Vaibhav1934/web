from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('',views.inner, name='inner'),
    path('courses.html',views.courses,name='courses'),
    path('index.html',views.index, name='index'),
    path('bcom.html',views.bcom, name='index'),
     path('bba.html',views.bba, name='index'),
      path('bsw.html',views.bsw, name='index'),
       path('bsc.html',views.bsc, name='index'),
        path('blis.html',views.blis, name='index'),
         path('mlis.html',views.mlis, name='index'),
          path('mba.html',views.mba, name='index'),
           path('ma.html',views.ma, name='index')
    
]
