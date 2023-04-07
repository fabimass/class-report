# Generated by Django 4.1.5 on 2023-04-07 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_sync'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('deadline', models.DateTimeField()),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='submissions.repo')),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('commits', models.ManyToManyField(blank=True, related_name='commits', to='submissions.commit')),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='submissions.repo')),
            ],
        ),
    ]