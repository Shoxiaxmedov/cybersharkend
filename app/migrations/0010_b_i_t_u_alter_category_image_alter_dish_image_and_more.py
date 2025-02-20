# Generated by Django 5.0.6 on 2024-07-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_profile_user_alter_profile_img_alter_purchase_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='I',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='T',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='U',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(upload_to='media//%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
