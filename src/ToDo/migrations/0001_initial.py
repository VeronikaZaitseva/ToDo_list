# Generated by Django 3.0.3 on 2020-02-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('check', models.BooleanField(default=False)),
                ('content', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('red', 'Red'), ('yellow', 'Yellow'), ('green', 'Green')], default='red', max_length=20)),
            ],
        ),
    ]
