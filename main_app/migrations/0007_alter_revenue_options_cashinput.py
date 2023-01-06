# Generated by Django 4.1.2 on 2023-01-06 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_revenue_yearly'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenue',
            options={'ordering': ['-date']},
        ),
        migrations.CreateModel(
            name='CashInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('atm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.atm')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
