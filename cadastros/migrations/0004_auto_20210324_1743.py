# Generated by Django 3.1.5 on 2021-03-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20210324_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saida',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
