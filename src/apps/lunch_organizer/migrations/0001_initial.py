# Generated by Django 4.2.2 on 2023-06-23 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_year', models.IntegerField(blank=True, help_text='Year in the current stage', null=True, verbose_name='classroom_year')),
                ('classroom_line', models.CharField(blank=True, help_text='Line in the current year', max_length=1, null=True, verbose_name='classroom_line')),
                ('stage', models.CharField(blank=True, choices=[('Infant', 'Infant'), ('Primary', 'Primary'), ('Secondary', 'Secondary')], help_text='Stage of the classroom', max_length=20, null=True, verbose_name='Stage')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Name of the student', max_length=50, null=True, verbose_name='Name')),
                ('surname', models.CharField(blank=True, help_text='Surname of the student', max_length=50, null=True, verbose_name='Surname')),
                ('allergies', models.CharField(blank=True, help_text='Allergies of the student', max_length=50, null=True, verbose_name='Allergies')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_organizer.classroom')),
            ],
        ),
    ]