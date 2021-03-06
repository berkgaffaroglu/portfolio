# Generated by Django 3.1 on 2020-10-05 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioRest', '0011_auto_20200815_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who_am_i', models.TextField()),
                ('what_are_my_technical_skills', models.TextField()),
                ('what_is_my_personality', models.TextField()),
                ('stackoverflow_link', models.CharField(blank=True, max_length=255, null=True)),
                ('github_link', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='backend_category',
            field=models.CharField(blank=True, choices=[('Django', 'Django'), ('Ruby', 'Ruby'), ('Python Application', 'Python Application'), ('Uncategorized', 'Uncategorized'), ('Node.js', 'Node.js'), ('Flask', 'Flask')], default='Uncategorized', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='frontend_category',
            field=models.CharField(blank=True, choices=[('React.js', 'React.js'), ('Angular.js', 'Angular.js'), ('Vue.js', 'Vue.js'), ('Uncategorized', 'Uncategorized')], default='Uncategorized', max_length=100, null=True),
        ),
    ]
