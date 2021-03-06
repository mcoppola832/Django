from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # /polls/5/
        url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
        # /polls/5/results/
        url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
        # /polls/5/vote/
        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
        )

