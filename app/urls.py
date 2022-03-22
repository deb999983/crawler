from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.ScheduleCrawlView.as_view(), name='queue-url-for-crawling'),
	re_path(r'^content/(?P<code>[a-z_\-\d]+)/$', views.CrawlContentView.as_view(), name='get-url-crawl-content')
]

