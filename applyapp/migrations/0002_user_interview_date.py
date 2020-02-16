# Generated by Django 3.0.3 on 2020-02-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='interview_date',
            field=models.CharField(choices=[('토', '21(토)'), ('일', '22(일)'), ('양일', '모두 가능')], max_length=10, null=True, verbose_name='인터뷰 가능일'),
        ),
    ]