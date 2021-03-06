# Generated by Django 3.0.8 on 2020-08-06 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('file', models.FileField(upload_to='')),
                ('entrega', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.Entregas')),
                ('subida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cursos.Subidas')),
            ],
        ),
    ]
