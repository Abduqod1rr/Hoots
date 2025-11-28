from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.Homeview.as_view(), name="home"),
    path("choot/", views.createHoot.as_view(), name="choot"),
    path("myhoots/", views.myhootsview.as_view(), name="myhoots"),#add button on home page!!!!
    path("delete/<int:pk>", views.deleteHoot.as_view(), name="delete"),
    path("update/<int:pk>", views.updateHoot.as_view(), name="update"),
    path("toggle_like/<int:pk>", views.toggle_like, name="toggle_like")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)