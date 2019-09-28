from django.conf import settings
from django.db import models
from django.utils import timezone

        
class VoteQuestion(models.Model):
    question = models.CharField(max_length=100, verbose_name='Текст вопроса')
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100, verbose_name='Изображение', null=True, blank=True)
    time_begin = models.DateTimeField(auto_now_add=True, verbose_name='Время начала')
    time_end = models.DateTimeField(auto_now=True, verbose_name='Время окончания')
    preamble = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Голосование - вопрос'
        verbose_name_plural = 'Голосование - вопросы'
        
    def __str__(self):
        return self.question
        
    
class VoteAnswer(models.Model):
    vote_question = models.ForeignKey(VoteQuestion, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField(max_length=30, verbose_name='Ответ')
    image = models.ImageField(upload_to='uploads/', height_field=None, width_field=None, max_length=100, verbose_name='Изображение', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Голосование - ответ'
        verbose_name_plural = 'Голосование - ответы'
        
    def __str__(self):
        return ' - '.join(map(str, [self.vote_question, self.text]))
        

class Quiz(models.Model):
    questions = models.ManyToManyField(VoteAnswer, verbose_name='Вопросы')
    preamble = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Опросник'
        verbose_name_plural = 'Опросник'
        
    def __str__(self):
        return self.questions
        

types = (
    (1, '1 выбор'),
    (2, 'много'),
    (3, 'текст')
)
class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name='Вопросы')
    text = models.CharField(verbose_name='Question text', max_length=100)
    type = models.IntegerField(verbose_name='Тип вопроса', choices=types)
    
    class Meta:
        verbose_name = 'Опросник - вопрос'
        verbose_name_plural = 'Опросник - вопрос'
        
    def __str__(self):
        return self.text
        
    
class QuizAnswer(models.Model):
    quiz_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, verbose_name='Вопрос')
    text = models.CharField(verbose_name='Question text', max_length=100)
    
    class Meta:
        verbose_name = 'Голосование - вопрос'
        verbose_name_plural = 'Голосование - вопросы'
        
    def __str__(self):
        return ' - '.join(map(str, [self.quiz_question, self.text]))
    

class VoteUsersAnswer(models.Model):
    vote_answer = models.ForeignKey(VoteAnswer, on_delete=models.CASCADE, verbose_name='Ответ пользователя')
    user_id = models.CharField(verbose_name='Идентификатор пользователя', max_length=30)

    class Meta:
        verbose_name = 'Голосование - список ответов'
        verbose_name_plural = 'Голосование - список ответов'
        
    def __str__(self):
        return ' - '.join(map(str, [self.vote_answer, self.user_id]))
    
    
class QuizUsersAnswer(models.Model):
    answer = models.CharField(verbose_name='Ответ пользователя', max_length=30)
    quiz_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, verbose_name='Вопрос')
    quiz_answer = models.ForeignKey(QuizAnswer, on_delete=models.CASCADE, verbose_name='Ответ')
    
    class Meta:
        verbose_name = 'Вопросник - список ответов'
        verbose_name_plural = 'Вопросник - список ответов'
        
    def __str__(self):
        return self.answer