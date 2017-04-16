# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text=b'A lable for URL config', unique_for_month=b'pub_date', max_length=63)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name=b'date published')),
                ('startups', models.ManyToManyField(related_name='blog_post', to='organizer.Startup')),
                ('tags', models.ManyToManyField(related_name='blog_post', to='organizer.Tag')),
            ],
            options={
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
                'verbose_name': 'blog post',
            },
        ),
    ]
