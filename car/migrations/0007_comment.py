# Generated by Django 4.1.2 on 2022-10-13 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_commented', models.DateField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.vehicle')),
            ],
        ),
    ]
