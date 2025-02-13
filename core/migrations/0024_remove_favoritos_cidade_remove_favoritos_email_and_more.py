# Generated by Django 5.1.3 on 2025-02-06 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_alter_favoritos_nome"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="favoritos",
            name="cidade",
        ),
        migrations.RemoveField(
            model_name="favoritos",
            name="email",
        ),
        migrations.RemoveField(
            model_name="favoritos",
            name="nome",
        ),
        migrations.RemoveField(
            model_name="favoritos",
            name="site",
        ),
        migrations.AddField(
            model_name="favoritos",
            name="livro",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="itens_favoritos",
                to="core.livro",
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="ItensFavoritos",
        ),
    ]
