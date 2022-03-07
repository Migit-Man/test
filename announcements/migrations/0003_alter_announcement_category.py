# Generated by Django 4.0.3 on 2022-03-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0002_announcement_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='category',
            field=models.CharField(choices=[('MRP', 'MilitaryRP'), ('DC', 'Discord'), ('WEB', 'Website'), ('COM', 'Community')], default='MRP', max_length=3),
        ),
    ]
