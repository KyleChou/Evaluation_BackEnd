# Generated by Django 2.2.3 on 2019-07-14 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpsite', '0006_remove_evaluationitem_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='semaster',
            new_name='semeser',
        ),
    ]
