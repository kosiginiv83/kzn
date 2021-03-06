# Generated by Django 2.2.5 on 2019-09-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_stat', '0002_auto_20190928_1308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Опросник', 'verbose_name_plural': 'Опросник'},
        ),
        migrations.AlterModelOptions(
            name='quizanswer',
            options={'verbose_name': 'Голосование - вопрос', 'verbose_name_plural': 'Голосование - вопросы'},
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={'verbose_name': 'Опросник - вопрос', 'verbose_name_plural': 'Опросник - вопрос'},
        ),
        migrations.AlterModelOptions(
            name='quizusersanswer',
            options={'verbose_name': 'Вопросник - список ответов', 'verbose_name_plural': 'Вопросник - список ответов'},
        ),
        migrations.AlterModelOptions(
            name='voteanswer',
            options={'verbose_name': 'Голосование - ответ', 'verbose_name_plural': 'Голосование - ответы'},
        ),
        migrations.AlterModelOptions(
            name='votequestion',
            options={'verbose_name': 'Голосование - вопрос', 'verbose_name_plural': 'Голосование - вопросы'},
        ),
        migrations.AlterModelOptions(
            name='voteusersanswer',
            options={'verbose_name': 'Голосование - список ответов', 'verbose_name_plural': 'Голосование - список ответов'},
        ),
        migrations.AddField(
            model_name='quiz',
            name='preamble',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votequestion',
            name='preamble',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voteanswer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='votequestion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Изображение'),
        ),
        migrations.DeleteModel(
            name='data',
        ),
    ]
