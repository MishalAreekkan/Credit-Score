# Generated by Django 5.1.3 on 2024-11-12 04:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit_score', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer_choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userresponse',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userresponse',
            name='answer',
            field=models.CharField(choices=[('A', 'Sometimes'), ('B', 'Never'), ('C', 'Always'), ('D', 'Nil')], max_length=9),
        ),
    ]
