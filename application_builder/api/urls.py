from django.urls import include, path
from rest_framework.routers import DefaultRouter


from api.applications.views import (ApplicationListCreateView,
                                    ApplicationRetrieveUpdateView)
from api.citizenships.views import CitizenshipViewSet
from api.languages.views import LanguageViewSet
from api.professions.views import ProfessionViewSet
from api.cities.views import CityViewSet
from api.users.views import obtain_auth_token


app_name = 'api'
VERSION = 'v2'

router = DefaultRouter()
router.register('citizenships', CitizenshipViewSet, basename='citizenship')
router.register('languages', LanguageViewSet, basename='language')
router.register('professions', ProfessionViewSet, basename='profession')
router.register('cities', CityViewSet, basename='city')


urlpatterns = [
    path(f'{VERSION}/auth/login/', obtain_auth_token, name='login'),
    path(f'{VERSION}/applications/',
         ApplicationListCreateView.as_view(),
         name='applications-list'),
    path(f'{VERSION}/applications/<int:pk>/',
         ApplicationRetrieveUpdateView.as_view(),
         name='applications-detail'),
    path(f'{VERSION}/', include(router.urls)),
]
