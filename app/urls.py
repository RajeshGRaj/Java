from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("", sign_up, name="sign_up"),
   path("loggin/", sign_in, name="sign_in"),
   path("profile/", profile, name="profile"),
   path("sign_out/", loggout, name="sign_out"),
   path("like/<int:id>", like, name="like"),
   path("post/", post, name="post_form"),
   #topic url
   path('topic/', topic, name='java'),
   path('details/<int:id>/', get_details, name='topic_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
