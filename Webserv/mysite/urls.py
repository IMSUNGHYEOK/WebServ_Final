from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
from mysite.views import (UserLoginView, UserLogoutView,
                          UserPasswordChangeView, UserPasswordChangeDoneView,
                          UserCreateView, UserCreateDoneTV)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/login/$', UserLoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', UserLogoutView.as_view(), name='logout'),
    url(r'^password_change/$', UserPasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', UserPasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
