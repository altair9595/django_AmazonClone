# Generated by Django 4.2.2 on 2023-07-03 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('image', models.ImageField(upload_to='brands', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('price', models.FloatField(verbose_name='price')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('description', models.TextField(max_length=30000, verbose_name='description')),
                ('subtitle', models.TextField(max_length=500, verbose_name='subtitle')),
                ('sku', models.IntegerField(verbose_name='sky')),
                ('image', models.ImageField(upload_to='products', verbose_name='image')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_brand', to='products.brand', verbose_name='brand')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=500, verbose_name='review')),
                ('rate', models.BigIntegerField(verbose_name='rate')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creat_date')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='products.product', verbose_name='product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='productimages', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product', verbose_name='product')),
            ],
        ),
    ]
