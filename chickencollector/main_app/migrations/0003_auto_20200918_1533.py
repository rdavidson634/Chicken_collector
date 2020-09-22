# Generated by Django 2.2.12 on 2020-09-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='chicken',
            name='toys',
            field=models.ManyToManyField(to='main_app.Toy'),
        ),
    ]
