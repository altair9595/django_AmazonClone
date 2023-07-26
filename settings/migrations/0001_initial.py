from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("logo", models.ImageField(blank=True, null=True, upload_to="company")),
                ("call_us", models.CharField(blank=True, max_length=20, null=True)),
                ("email_us", models.EmailField(blank=True, max_length=254, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("subtitle", models.CharField(blank=True, max_length=200, null=True)),
                ("emails", models.TextField(blank=True, max_length=200, null=True)),
                ("phones", models.TextField(blank=True, max_length=200, null=True)),
                ("fb_link", models.URLField(blank=True, null=True)),
                ("twitter_link", models.URLField(blank=True, null=True)),
                ("youtube_link", models.URLField(blank=True, null=True)),
                ("android_app", models.URLField(blank=True, null=True)),
                ("ios_app", models.URLField(blank=True, null=True)),
            ],
        ),
    ]