# Generated by Django 3.2.5 on 2021-08-18 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_post', '0002_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='user_account.account'),
            preserve_default=False,
        ),
    ]
