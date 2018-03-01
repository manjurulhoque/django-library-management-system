from django.conf.urls import url

from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    url(r'login$', login_view, name='login'),
    url(r'signup', register_view, name='signup'),
    url(r'logout', logout_view, name='logout'),
]