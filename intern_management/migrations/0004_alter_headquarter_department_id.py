# Generated by Django 4.2.3 on 2023-07-21 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intern_management', '0003_rename_studentresult_internresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headquarter',
            name='department_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='intern_management.department'),
        ),
    ]