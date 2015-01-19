from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'chatroom.views.home'),
    url(r'^send-message$', 'chatroom.views.send_message'),
    url(r'^register$', 'chatroom.views.register'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'htmlfiles/login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
)
