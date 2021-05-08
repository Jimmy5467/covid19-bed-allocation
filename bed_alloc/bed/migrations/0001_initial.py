# Generated by Django 3.2 on 2021-05-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=300)),
                ('lname', models.CharField(max_length=300)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('ct', models.IntegerField()),
                ('oxy', models.IntegerField()),
                ('oc', models.IntegerField()),
                ('ct_pdf', models.FileField(upload_to='')),
            ],
        ),
    ]
