# Generated by Django 5.0.6 on 2024-06-29 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_purchase_delete_bandqilish_remove_reservation_pc_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name_plural': 'Profile Table'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
