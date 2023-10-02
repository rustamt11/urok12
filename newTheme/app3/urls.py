from django.urls import path
from app2.views import func_one

urlpatterns = [
    # 127.0.0.1:8000/theme/
    path("func1/", func_one),
]