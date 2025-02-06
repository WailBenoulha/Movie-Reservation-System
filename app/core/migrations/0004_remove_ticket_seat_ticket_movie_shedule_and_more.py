# Generated by Django 5.1.5 on 2025-02-05 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_seats_number_normal_seats_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="seat",
        ),
        migrations.AddField(
            model_name="ticket",
            name="movie_shedule",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.movie_shedules",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticket",
            name="seat_type",
            field=models.CharField(
                choices=[("vip", "Vip"), ("normal", "Normal")],
                default=3,
                max_length=255,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="seats",
            name="movie_time_infos",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="core.movie_shedules"
            ),
        ),
    ]
