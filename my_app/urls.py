from django.conf.urls import url
import my_app.views as views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^done/$', views.done, name='done')
]
