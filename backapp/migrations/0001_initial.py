# Generated by Django 2.2.4 on 2019-08-04 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsname', models.CharField(max_length=50)),
                ('item', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('date', models.DateTimeField(verbose_name='date')),
            ],
        ),
    ]