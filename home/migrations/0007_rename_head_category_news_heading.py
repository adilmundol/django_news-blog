# Generated by Django 5.1.2 on 2024-11-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_news_heading'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Head',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='news',
            name='heading',
            field=models.CharField(default=11, max_length=30),
            preserve_default=False,
        ),
    ]