# Generated by Django 4.2.1 on 2023-12-13 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HiddenHarbor', '0008_answers_score_question_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='LikeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='LikeCount',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='LikeQus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiddenHarbor.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeAns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiddenHarbor.answers')),
                ('qus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HiddenHarbor.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
