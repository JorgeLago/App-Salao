# Generated by Django 4.1.3 on 2023-01-07 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='nome',
            new_name='descricao',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='data',
            field=models.DateTimeField(default=12),
            preserve_default=False,
        ),
    ]
