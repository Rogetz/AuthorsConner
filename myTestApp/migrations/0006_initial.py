# Generated by Django 4.1.13 on 2024-02-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myTestApp', '0005_delete_mybookmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='enter title of the book', max_length=20)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
