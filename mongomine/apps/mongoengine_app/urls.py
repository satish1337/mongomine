from django.conf.urls import patterns, include
from rest_framework import routers

from . import views as mongoengine_views

candidate_router = routers.SimpleRouter()
candidate_router.register('candidate', mongoengine_views.CandidateViewSet, 'candidate')

urlpatterns = patterns(
    '',
    (r'^', include(candidate_router.urls)),
)