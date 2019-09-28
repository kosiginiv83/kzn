from django.contrib import admin
from .models import VoteQuestion, VoteAnswer, Quiz, QuizQuestion, QuizAnswer, VoteUsersAnswer, QuizUsersAnswer

admin.site.register(VoteUsersAnswer)
admin.site.register(QuizUsersAnswer)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)


class VoteAnswerTabularInline(admin.TabularInline):
    model = VoteAnswer


@admin.register(VoteQuestion)
class VoteQuestionAdmin(admin.ModelAdmin):
    inlines = [VoteAnswerTabularInline, ]


class QuizAnswerTabularInline(admin.TabularInline):
    model = QuizAnswer


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [QuizAnswerTabularInline, ]
