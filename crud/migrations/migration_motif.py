# Generated by Django 2.2.6 on 2019-10-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='motifs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('motif_Img', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'motifs',
            },
        ),
    ]