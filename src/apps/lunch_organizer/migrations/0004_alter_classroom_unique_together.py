# Generated by Django 4.2.2 on 2023-06-24 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_organizer', '0003_alter_classroom_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classroom',
            unique_together={('classroom_year', 'classroom_line', 'stage')},
        ),
    ]
