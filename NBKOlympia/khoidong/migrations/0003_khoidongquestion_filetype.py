# Generated by Django 2.2.3 on 2019-08-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khoidong', '0002_auto_20190805_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='khoidongquestion',
            name='fileType',
            field=models.CharField(blank=True, choices=[('sound', 'Âm thanh'), ('video', 'Video'), ('image', 'Hình ảnh')], max_length=10, verbose_name='Loại file'),
        ),
    ]