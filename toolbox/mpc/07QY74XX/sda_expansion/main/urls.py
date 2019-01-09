from django.conf.urls import url

from . import views
#from .views import EquipmentList#, EquipmentView

urlpatterns = [
    #url(r'^$', views.equip_req, name='equip'),
    #url(r'show/(?P<pk>[0-9]+)$', EquipmentView.as_view(), name='equipment-detail'),
    url(r'equip$', EquipmentList.as_view(), name='show-equipment'
    ),
]

'''
from django.conf.urls import url

from . import views
from .views import ProjectList

urlpatterns = [
    url(r'projectlist', ProjectList.as_view(), name='show-projects'
    ),
]
'''
