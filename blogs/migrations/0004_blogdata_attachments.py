# Generated by Django 4.2.7 on 2023-11-09 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_like_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdata',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='post_attachments/'),
        ),
    ]
