# Generated by Django 5.0.6 on 2024-07-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_b_i_t_u_alter_category_image_alter_dish_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b',
            name='img',
            field=models.ImageField(upload_to='media/media/'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
