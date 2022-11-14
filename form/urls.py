from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('form/',views.studentform_form, name='studentform_form'),
    path('form/all_student.html',views.allstudents, name='allstudents'),
    path('form/<int:id>/edit.html',views.edit, name='edit'),
    path('form/search.html',views.search, name='search'),
    path('form/search_result.html',views.result, name='result'),
    # path('',views.ReportstudentListView.as_view(),name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)