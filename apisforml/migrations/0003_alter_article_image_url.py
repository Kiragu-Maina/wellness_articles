# Generated by Django 4.2.4 on 2023-08-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apisforml', '0002_alter_article_author_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]