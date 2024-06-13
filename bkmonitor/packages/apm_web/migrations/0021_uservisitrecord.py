# Generated by Django 3.2.15 on 2024-06-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apm_web', '0020_profileuploadrecord_data_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVisitRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bk_biz_id', models.BigIntegerField(verbose_name='业务 ID')),
                ('app_name', models.CharField(max_length=50, null=True, verbose_name='应用名称')),
                ('func_name', models.CharField(default='', max_length=128, verbose_name='功能名称')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='访问时间')),
                ('created_by', models.CharField(db_index=True, default='', max_length=32, verbose_name='访问者')),
            ],
            options={
                'verbose_name': 'APM 用户访问记录',
                'verbose_name_plural': 'APM 用户访问记录',
            },
        ),
    ]