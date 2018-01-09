from django.conf.urls import url

from .views import LucasListView, LucasDetailView

urlpatterns = [
    url(r'(?P<pk>\d+)/$', LucasDetailView.as_view(), name='detail'),
    url(r'$', LucasListView.as_view(), name='list'),
]
