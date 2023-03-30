"""
Determines the URL conf for Finder app API using routers to automatically
register all the endpoints with the corresponding View/Viewset.
"""

from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "finder"


class FinderApiView(routers.APIRootView):
    """Finder App API Root View"""

    pass


class FinderRouter(routers.DefaultRouter):
    """Finder Router"""

    APIRootView = FinderApiView


router = FinderRouter()
router.register(r"findings", views.FindingViewSet, basename="finding")

urlpatterns = [
    path("", include(router.urls)),
]
