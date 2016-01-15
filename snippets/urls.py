from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
    url(r'^author/$',views.author_list),
    url(r'^author/(?P<pk>[0-9]+)/$',views.author_detail),
    url(r'^hello/$',views.hello, name='hello'),
    url(r'^new/$',views.new, name='new'),
    url(r'^note/$',views.note, name='note'),
    url(r'^mark/(?P<pk>[0-9]+)/$', views.mark_detail),
    url(r'^mark/$',views.mark_list),
    url(r'^note/(?P<pk>[0-9]+)/$', views.note_detail),
    url(r'^note/$',views.note_list),
    url(r'^jjj/$',views.jjj, name='jjj'),
    url(r'^iii/$',views.iii, name='iii'),
    url(r'^kkk/$',views.kkk, name='kkk'),
    url(r'^hard/$', views.HardList.as_view()),
    url(r'^hard/(?P<pk>[0-9]+)/$', views.HardDetail.as_view()),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^soft/$', views.SoftList.as_view()),
    url(r'^soft/(?P<pk>[0-9]+)/$', views.SoftDetail.as_view()),
    url(r'^book/$', views.BookList.as_view()),
    url(r'^book/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
