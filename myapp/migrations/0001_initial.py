# Generated by Django 2.2.28 on 2023-08-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myImage')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
