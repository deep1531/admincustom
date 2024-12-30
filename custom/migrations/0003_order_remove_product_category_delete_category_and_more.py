# Generated by Django 4.2.16 on 2024-12-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_alter_category_jeans_section_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='order_images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]