# Generated by Django 4.2.1 on 2023-12-02 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiddenHarbor', '0006_question_showauthorname'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='allowPrivateMessages',
            field=models.BooleanField(default=False),
        ),
    ]