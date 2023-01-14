# Generated by Django 4.1.5 on 2023-01-14 12:09

from django.db import migrations

def create_profiles(apps, schema_editor):

    User = apps.get_model('auth', 'User')

    Profile = apps.get_model('accounts', 'Profile')

    for user in User.objects.all():

        Profile.objects.get_or_create(user=user)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20230114_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),

        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]
