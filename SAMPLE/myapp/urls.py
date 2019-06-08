from django.conf.urls import include, url


urlpatterns = [
   url(r'^hello/', 'hello', name = 'hello'),
   url(r'^morning/', 'morning', name = 'morning'),
]