from rest_framework import serializers
from .models import VoteQuestion, VoteAnswer, Quiz, QuizQuestion, QuizAnswer, VoteUsersAnswer, QuizUsersAnswer


class VoteQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteQuestion
        fields = ('id', 'text', 'image')
        

class VoteAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteAnswer
        fields = ('id', 'text', 'image')
        

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'questions')
        
        
class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ('id', 'text', 'type')
        
        
class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = ('id', 'text')
        
        
class VoteUsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteUsersAnswer
        fields = ('id', 'user_id')
        
        
class QuizUsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizUsersAnswer
        fields = ('id', 'answer', 'quiz_question', 'quiz_answer')