# Generated by Django 2.1.7 on 2019-03-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0007_auto_20190130_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag_loading', '-auto_load', 'tag_location', '-priority']},
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='active',
            new_name='auto_load',
        ),
        migrations.AlterField(
            model_name='tag',
            name='auto_load',
            field=models.BooleanField(default=True, help_text='Uncheck to disable this tag from being included automatically, or when using a trigger to include this tag.'),
        ),
    ]