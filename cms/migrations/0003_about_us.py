# Generated by Django 4.2.1 on 2023-06-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_rename_faq_faqs_alter_faqs_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='team')),
            ],
        ),
    ]
