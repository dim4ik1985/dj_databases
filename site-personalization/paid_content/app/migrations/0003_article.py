# Generated by Django 2.1.1 on 2018-09-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180905_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Заголовок')),
                ('content', models.TextField(max_length=2048, verbose_name='Содержимое')),
                ('pay', models.BooleanField(verbose_name='Платный контент')),
            ],
        ),
    ]
