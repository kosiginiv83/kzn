from rest_framework import serializers
from .models import VoteQuestion, VoteAnswer, Quiz, QuizQuestion, QuizAnswer, VoteUsersAnswer, QuizUsersAnswer


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ('id', 'text')


class VoteUsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteUsersAnswer
        fields = ('id', 'user_id')


class QuizQuestionSerializer(serializers.ModelSerializer):
    answers = QuizAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = QuizQuestion
        fields = ('id', 'text', 'type', 'answers')


class QuizSerializer(serializers.ModelSerializer):
    qquestions = QuizQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ('id', 'questions', 'qquestions')


class VoteAnswerSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = VoteAnswer
        fields = ('id', 'text', 'image', 'quiz')


class VoteQuestionSerializer(serializers.ModelSerializer):
    answers = VoteAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = VoteQuestion
        fields = ('id', 'question', 'image', 'answers')


class QuizUsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizUsersAnswer
        fields = ('id', 'answer', 'quiz_question', 'quiz_answer')
