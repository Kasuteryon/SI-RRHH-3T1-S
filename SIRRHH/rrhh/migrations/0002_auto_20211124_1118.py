# Generated by Django 3.2.9 on 2021-11-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catclausulas',
            fields=[
                ('idcatclausula', models.AutoField(db_column='IdCatClausula', primary_key=True, serialize=False)),
                ('numclausula', models.IntegerField(db_column='NumClausula')),
                ('clausula', models.TextField(db_column='Clausula')),
                ('estado', models.TextField(db_column='Estado')),
            ],
            options={
                'db_table': 'catclausulas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clausulacontrato',
            fields=[
                ('idclausulacontrato', models.AutoField(db_column='IdClausulaContrato', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(db_column='Fecha')),
            ],
            options={
                'db_table': 'clausulacontrato',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Clausulascontrato',
        ),
    ]