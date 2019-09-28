from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import QuizAnswerViewSet, QuizQuestionViewSet, VoteAnswerViewSet, VoteQuestionViewSet, \
    VoteUsersAnswerViewSet, QuizUsersAnswerViewSet, QuizViewSet
from phones.views import PhoneViewSet

router = routers.DefaultRouter()
router.register(r'vote', VoteQuestionViewSet)
router.register(r'phone', PhoneViewSet, base_name='phone')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
