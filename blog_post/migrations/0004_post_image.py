# Generated by Django 3.2.5 on 2021-08-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0003_auto_20210818_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='post_pics/default.jpg', null=True, upload_to='post_pics'),
        ),
    ]
