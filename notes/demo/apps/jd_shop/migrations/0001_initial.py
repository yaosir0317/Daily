# Generated by Django 2.1.4 on 2019-03-29 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JdCategoryModel',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('create_time', models.CharField(default='', help_text='创建时间', max_length=13, verbose_name='创建时间')),
                ('is_home_show', models.BooleanField(default=False)),
                ('is_open', models.BooleanField(default=False)),
                ('modify_time', models.CharField(default='', help_text='更新时间', max_length=13, verbose_name='更新时间')),
                ('name', models.CharField(default='', help_text='店类分类名称', max_length=64, verbose_name='店类分类名称')),
                ('order_no', models.IntegerField(default=0)),
                ('parent_cid', models.IntegerField(default=0)),
                ('status', models.SmallIntegerField(default=1)),
                ('vender_id', models.IntegerField(default=0, help_text='商家编号', verbose_name='商家编号')),
            ],
            options={
                'verbose_name': '京东后台类目信息',
                'verbose_name_plural': '京东后台类目信息',
                'db_table': 'jd_category',
            },
        ),
        migrations.CreateModel(
            name='JdShopInfoModel',
            fields=[
                ('shop_id', models.IntegerField(help_text='店铺唯一ID', primary_key=True, serialize=False, verbose_name='店铺ID')),
                ('shop_name', models.CharField(default='', help_text='店铺名称', max_length=64, verbose_name='店铺名称')),
                ('open_time', models.CharField(default='', help_text='开店时间', max_length=64, verbose_name='开店时间')),
                ('vender_id', models.IntegerField(default=0, help_text='商家编号', verbose_name='商家编号')),
                ('brief', models.TextField(default='', help_text='商家简介', verbose_name='商家简介')),
                ('logo_url', models.CharField(default='', help_text='商家Logo', max_length=128, verbose_name='商家Logo')),
                ('category_main', models.IntegerField(default=0, help_text='主营类目ID', verbose_name='主营类目ID')),
                ('category_main_name', models.CharField(default='', help_text='主营类目名称', max_length=64, verbose_name='主营类目名称')),
            ],
            options={
                'verbose_name': '店铺基础信息',
                'verbose_name_plural': '店铺基础信息',
                'db_table': 'jd_shop_info',
            },
        ),
        migrations.AddField(
            model_name='jdcategorymodel',
            name='shop_info',
            field=models.ForeignKey(help_text='店铺信息', on_delete=django.db.models.deletion.CASCADE, related_name='shop_info', to='jd_shop.JdShopInfoModel', verbose_name='店铺信息'),
        ),
    ]
