# Generated by Django 3.1.7 on 2021-03-29 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_auto_20210328_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saida',
            name='detalhes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.produtos_entrada'),
        ),
    ]
