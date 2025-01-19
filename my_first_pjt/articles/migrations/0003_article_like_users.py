# Generated by Django 4.2 on 2025-01-19 06:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0002_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Like_users',
            field=models.ManyToManyField(related_name='Like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]