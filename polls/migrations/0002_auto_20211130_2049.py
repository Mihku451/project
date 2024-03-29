# Generated by Django 3.1.4 on 2021-11-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='visible_valid_answers',
        ),
        migrations.AddField(
            model_name='exercise',
            name='time',
            field=models.IntegerField(default=120),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_type',
            field=models.CharField(choices=[('radio', 'один из'), ('checkbox', 'несколько из'), ('textbox', 'Ввод текста')], default='radio', max_length=16),
        ),
    ]
