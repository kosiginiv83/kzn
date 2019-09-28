from django.contrib import admin
from .models import VoteQuestion, VoteAnswer, Quiz, QuizQuestion, QuizAnswer, VoteUsersAnswer, QuizUsersAnswer

admin.site.register(Quiz)
admin.site.register(VoteUsersAnswer)
admin.site.register(QuizUsersAnswer)


class VoteAnswerTabularInline(admin.TabularInline):
    model = VoteAnswer


@admin.register(VoteQuestion)
class VoteQuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    list_display_links = ('text',)
    inlines = [VoteAnswerTabularInline, ]


class QuizAnswerTabularInline(admin.TabularInline):
    model = QuizAnswer


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    inlines = [QuizAnswerTabularInline, ]
