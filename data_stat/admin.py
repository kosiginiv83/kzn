from django.contrib import admin
from .models import VoteQuestion, VoteAnswer, Quiz, QuizQuestion, QuizAnswer, VoteUsersAnswer, QuizUsersAnswer


admin.site.register(VoteQuestion)
admin.site.register(VoteAnswer)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)
admin.site.register(VoteUsersAnswer)
admin.site.register(QuizUsersAnswer)