# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-02 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_auto_20180702_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityimagesmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityImagesModel/%y/%d/9c0fa8d569f640dbb7fd73737e0efafd', verbose_name='活动图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='activitytype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activitytype', to='activity.ActivityTypeModel', verbose_name='活动类别'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='audit',
            field=models.CharField(choices=[('0', '审核中'), ('1', '审核通过')], default=0, max_length=1, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/%y/%d/9c0fa8d569f640dbb7fd73737e0efafd', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='activitymodel',
            name='groupcode',
            field=models.ImageField(blank=True, null=True, upload_to='Activity/qr/%y/%d/9c0fa8d569f640dbb7fd73737e0efafd', verbose_name='群二维码'),
        ),
        migrations.AlterField(
            model_name='activitytypemodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='ActivityTypeModel/%y/%d/9c0fa8d569f640dbb7fd73737e0efafd', verbose_name='类别图片'),
        ),
        migrations.AlterField(
            model_name='slidemodels',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='SlideModels/%y/%d/9c0fa8d569f640dbb7fd73737e0efafd', verbose_name='幻灯片图片'),
        ),
    ]
