from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user$', views.user, name='user'),
    url(r'^game$', views.game, name='game'),
	url(r'^check$',views.check, name='check'),
]
