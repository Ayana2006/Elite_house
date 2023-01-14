# Generated by Django 4.1.4 on 2023-01-12 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=255)),
                ('location', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('architetor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='architetor', to='team.team')),
            ],
            options={
                'verbose_name': 'Здание',
                'verbose_name_plural': 'Здания',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='building_images/')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='buildings.building')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]
