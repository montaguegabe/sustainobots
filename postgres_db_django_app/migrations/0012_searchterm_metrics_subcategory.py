# Generated by Django 5.1.3 on 2024-11-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postgres_db_django_app", "0011_searchterm_metrics_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="searchterm",
            name="metrics_subcategory",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
