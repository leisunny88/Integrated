# Generated by Django 2.1 on 2020-07-31 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('weibo', '微博'), ('google', '谷歌'), ('github', 'GitHub'), ('facebook', 'FaceBook'), ('qq', 'QQ')], default='a', max_length=10, verbose_name='类型')),
                ('appkey', models.CharField(max_length=200, verbose_name='AppKey')),
                ('appsecret', models.CharField(max_length=200, verbose_name='AppSecret')),
                ('callback_url', models.CharField(default='http://www.baidu.com', max_length=200, verbose_name='回调地址')),
                ('is_enable', models.BooleanField(default=True, verbose_name='是否显示')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': 'oauth配置',
                'verbose_name_plural': 'oauth配置',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='OAuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50)),
                ('nikename', models.CharField(max_length=50, verbose_name='昵称')),
                ('token', models.CharField(blank=True, max_length=150, null=True)),
                ('picture', models.CharField(blank=True, max_length=350, null=True)),
                ('type', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('matedata', models.TextField(blank=True, null=True)),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'oauth用户',
                'verbose_name_plural': 'oauth用户',
                'ordering': ['-created_time'],
            },
        ),
    ]
