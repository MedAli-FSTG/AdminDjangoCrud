from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('add', views.add),
    path('create', views.create),  # create method url
    # read method url but here, null because type localhost show read view
    path('', views.read),
    path('update/<id>', views.update),  # update method url
    path('delete/<id>', views.delete),  # delete method url
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
