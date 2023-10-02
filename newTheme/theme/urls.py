from django.urls import path
from theme.views import miles, duke, john, charlie


urlpatterns = [
    # 127.0.0.1:8000/theme/
    path("miles/", miles),
    path("duke/", duke),
    path("john/", john),
    path("charlie/", charlie),

]