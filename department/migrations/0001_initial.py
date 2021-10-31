# Generated by Django 3.2.3 on 2021-05-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
                ('department_code', models.CharField(blank=True, max_length=10)),
                ('department_description', models.TextField()),
            ],
            options={
                'ordering': ('department_name',),
            },
        ),
    ]