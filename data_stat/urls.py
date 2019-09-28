from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import QuizAnswerViewSet, QuizQuestionViewSet, VoteAnswerViewSet, VoteQuestionViewSet, \
    VoteUsersAnswerViewSet, QuizUsersAnswerViewSet, QuizViewSet

router = routers.DefaultRouter()
router.register(r'vote', VoteQuestionViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
