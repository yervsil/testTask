# Generated by Django 4.1.5 on 2023-01-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Отправлен', 'Отправлен'), ('Отказ', 'Отказ'), ('Скоро свяжемся', 'Скоро свяжемся'), ('Принят в работу', 'Принят в работу')], default='Скоро свяжемся', max_length=20, null=True),
        ),
    ]