# Generated by Django 3.1 on 2020-08-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioRest', '0006_auto_20200815_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='backend_category',
            field=models.CharField(blank=True, choices=[('Flask', 'Flask'), ('Uncategorized', 'Uncategorized'), ('Node.js', 'Node.js'), ('Django', 'Django'), ('Ruby', 'Ruby'), ('Python Application', 'Python Application')], default='Uncategorized', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='frontend_category',
            field=models.CharField(blank=True, choices=[('React.js', 'React.js'), ('Vue.js', 'Vue.js'), ('Uncategorized', 'Uncategorized'), ('Angular.js', 'Angular.js')], default='Uncategorized', max_length=100, null=True),
        ),
    ]