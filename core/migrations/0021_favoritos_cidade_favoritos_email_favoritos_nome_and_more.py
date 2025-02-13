# Generated by Django 5.1.3 on 2025-02-03 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0020_remove_favoritos_cidade_remove_favoritos_email_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="favoritos",
            name="cidade",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="favoritos",
            name="email",
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="favoritos",
            name="nome",
            field=models.CharField(default="Nome Padrão", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="favoritos",
            name="site",
            field=models.URLField(blank=True, null=True),
        ),
    ]
