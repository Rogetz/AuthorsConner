# Generated by Django 4.1.13 on 2024-02-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myTestApp', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybookmodel',
            name='author',
            field=models.CharField(default='I Fixed it', help_text="author's name", max_length=20),
            preserve_default=False,
        ),
    ]
