# Generated by Django 3.1 on 2021-04-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioRest', '0017_auto_20210429_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='backend_category',
            field=models.CharField(blank=True, choices=[('Uncategorized', 'Uncategorized'), ('Node.js', 'Node.js'), ('Python Application', 'Python Application'), ('Django', 'Django'), ('Ruby', 'Ruby'), ('Flask', 'Flask')], default='Uncategorized', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='frontend_category',
            field=models.CharField(blank=True, choices=[('Angular.js', 'Angular.js'), ('React.js', 'React.js'), ('Uncategorized', 'Uncategorized'), ('Vue.js', 'Vue.js')], default='Uncategorized', max_length=100, null=True),
        ),
    ]
