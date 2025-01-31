# Generated by Django 5.0.3 on 2024-03-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField()),
                ('intensity', models.IntegerField(blank=True, null=True)),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.IntegerField(blank=True, null=True)),
                ('impact', models.CharField(blank=True, max_length=100, null=True)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(max_length=100)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
