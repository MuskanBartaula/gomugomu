# Generated by Django 3.2.4 on 2021-06-21 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40, verbose_name='activation')),
                ('activation_key', models.CharField(max_length=40, verbose_name='activation key')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100)),
                ('seller_email', models.CharField(blank=True, max_length=100)),
                ('product_type', models.CharField(blank=True, max_length=100)),
                ('product_quantity', models.CharField(blank=True, max_length=100)),
                ('product_reviews', models.CharField(blank=True, max_length=100)),
                ('product_website', models.CharField(blank=True, max_length=100)),
                ('product_relevant_page', models.CharField(blank=True, max_length=100)),
                ('product_status', models.CharField(default='0', max_length=100)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(blank=True, max_length=255)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_added_by', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='vvouch.products')),
            ],
        ),
    ]
