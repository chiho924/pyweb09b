from django.conf.urls import url

from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view
from myblog.views import post_list
from myblog.views import post_detail
from myblog.views import category_list
from myblog.views import category_detail

from rest_framework.urlpatterns import format_suffix_patterns
from myblog import views

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name='blog_detail'),
    url(r'^post/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)