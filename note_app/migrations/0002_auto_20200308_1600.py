# Generated by Django 2.2.10 on 2020-03-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='img',
            field=models.ImageField(default='', upload_to='note-img'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
