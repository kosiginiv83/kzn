from rest_framework import viewsets, decorators, response
from .models import VoteQuestion, VoteAnswer, Quiz, QuizAnswer, QuizQuestion, QuizUsersAnswer, VoteUsersAnswer
from .serializers import VoteQuestionSerializer, VoteAnswerSerializer, QuizSerializer, QuizQuestionSerializer, \
    QuizAnswerSerializer, VoteUsersAnswerSerializer, QuizUsersAnswerSerializer
import datetime

class VoteQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = VoteQuestionSerializer
    queryset = VoteQuestion.objects.all()
    http_method_names = ['get', ]

    @decorators.action(methods=['get'], detail=False, url_path='current', url_name='current')
    def current(self, request):
        instance = self.queryset.filter(time_begin__lte=datetime.datetime.now(), time_end__gte=datetime.datetime.now()).first()
        return response.Response(self.serializer_class(instance).data)



class VoteAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = VoteAnswerSerializer
    queryset = VoteAnswer.objects.all()
    http_method_names = ['get', ]


class QuizViewSet(viewsets.ModelViewSet):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    http_method_names = ['get', ]


class QuizQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuizQuestionSerializer
    queryset = QuizQuestion.objects.all()
    http_method_names = ['get', ]


class QuizAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = QuizAnswerSerializer
    queryset = QuizAnswer.objects.all()
    http_method_names = ['get', ]


class VoteUsersAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = VoteUsersAnswerSerializer
    queryset = VoteUsersAnswer.objects.all()
    http_method_names = ['get', ]


class QuizUsersAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = QuizUsersAnswerSerializer
    queryset = QuizUsersAnswer.objects.all()
    http_method_names = ['get', ]
