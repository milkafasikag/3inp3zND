# Generated by Django 4.2.4 on 2023-10-25 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_simage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='client_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Client_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.PositiveIntegerField(default=0, help_text='Width of the image in pixels')),
                ('height', models.PositiveIntegerField(default=0, help_text='Height of the image in pixels')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fuchers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.BooleanField(default=False)),
                ('message', models.BooleanField(default=False)),
                ('testmonial', models.BooleanField(default=False)),
                ('service', models.BooleanField(default=False)),
                ('prodact', models.BooleanField(default=False)),
                ('blog', models.BooleanField(default=False)),
                ('social', models.BooleanField(default=False)),
                ('worker', models.BooleanField(default=False)),
                ('booking', models.BooleanField(default=False)),
                ('about', models.BooleanField(default=False)),
                ('contact', models.BooleanField(default=False)),
                ('map', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='socilamedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='socilamedia_worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('social_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.socilamedia')),
            ],
        ),
        migrations.CreateModel(
            name='testmone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postion', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='services/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('socilamedia_worker', models.ManyToManyField(default=None, null=True, to='web.socilamedia_worker')),
            ],
        ),
        migrations.CreateModel(
            name='socilamedia_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('social_media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.socilamedia')),
            ],
        ),
    ]
