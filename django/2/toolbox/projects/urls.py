from django.conf.urls import url

from . import views
from .views import ProjectList

urlpatterns = [
    url(r'projectlist', ProjectList.as_view(), name='show-projects'
    ),
]