# Generated by Django 3.1.5 on 2021-04-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0011_auto_20210403_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisao',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='revisao',
            name='horimetro_revisao',
            field=models.IntegerField(verbose_name='Horímetro da revisão'),
        ),
    ]
