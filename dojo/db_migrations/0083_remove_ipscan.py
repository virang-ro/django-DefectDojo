# Generated by Django 2.2.17 on 2021-03-03 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0082_last_status_update_populate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scan',
            name='scan_settings',
        ),
        migrations.RemoveField(
            model_name='scansettings',
            name='product',
        ),
        migrations.RemoveField(
            model_name='scansettings',
            name='user',
        ),
        migrations.RemoveField(
            model_name='va',
            name='result',
        ),
        migrations.RemoveField(
            model_name='va',
            name='user',
        ),
        migrations.DeleteModel(
            name='IPScan',
        ),
        migrations.DeleteModel(
            name='Scan',
        ),
        migrations.DeleteModel(
            name='ScanSettings',
        ),
        migrations.DeleteModel(
            name='VA',
        ),
    ]