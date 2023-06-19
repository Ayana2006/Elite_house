from django.urls import path 
from apps.buildings.views import building_detail,building_index, response
urlpatterns = [
    path('<int:id>/', building_detail, name='building_detail'),
    path('', building_index, name='building_index'),
    path('response/', response, name='response'),

]