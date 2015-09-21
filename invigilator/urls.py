from django.conf.urls import patterns, include, url
from invigilator import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ctcm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'invigilator.views.home', name='home'),
    #url(r'^invigilatorList$',views.invigilator_list.as_view(), name='invigilatorList'),
    url(r'^invigilator_list/(?P<so>.*)/$','invigilator.views.invigilator_list', name='invigilatorList'),
    url(r'^invigilator_detail/(?P<invig_id>\d+)/$','invigilator.views.invigilator_detail', name='invigilatorDetail'),
    url(r'^createtestinvigs/(?P<num>\d+)/$','invigilator.tests.createtestinvigs', name='testinvigs'),
    url(r'^createinstitutions$','invigilator.tests.createinstitutions', name='testinstitutions'),
    
)
