# Generated by Django 4.2.6 on 2023-10-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaceRecognition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
