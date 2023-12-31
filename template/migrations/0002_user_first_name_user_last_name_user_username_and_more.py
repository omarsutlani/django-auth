# Generated by Django 4.2.4 on 2023-09-20 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('template', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Unknown', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='Unknown', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='Unknown', max_length=80, verbose_name='email'),
        ),
        migrations.CreateModel(
            name='UserProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='default.jpg', upload_to='uploads')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='template.user')),
            ],
        ),
    ]
