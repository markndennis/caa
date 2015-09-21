from django.conf.urls import patterns, include, url
from exams import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^createexamtype$','exams.tests.createexamtype', name='testexamtype'),
    url(r'^createques$','exams.tests.createques', name='testques'),
    url(r'^createexams$','exams.tests.createexams', name='testexams'),
    #url(r'^question/(?P<num>\d+)/$','exams.views.displayques', name='displayques'),
    url(r'^question$','exams.views.displayques', name='displayques'),
    url(r'^postanswer$','exams.views.postanswer', name='postanswer'),
    url(r'^intro$','exams.views.intro', name='intro'),
    url(r'^startexam$','exams.views.startexam', name='startexam'),
    #url(r'^myexam$','exams.views.myexam', name='myexam'),
)
