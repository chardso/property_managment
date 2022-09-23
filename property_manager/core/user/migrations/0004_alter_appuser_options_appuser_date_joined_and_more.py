# Generated by Django 4.1.1 on 2022-09-23 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core_user", "0003_alter_appuser_phone_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appuser",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AddField(
            model_name="appuser",
            name="date_joined",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date joined"
            ),
        ),
        migrations.AddField(
            model_name="appuser",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="appuser",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
        migrations.AddField(
            model_name="appuser",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether the user can log into this admin site.",
                verbose_name="staff status",
            ),
        ),
        migrations.AddField(
            model_name="appuser",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
    ]
