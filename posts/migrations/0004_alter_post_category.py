# Generated by Django 4.2.7 on 2023-12-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('technology', 'Technology'), ('fashion', 'Fashion'), ('cars', 'Cars'), ('sports', 'Sports'), ('health', 'Health'), ('politics', 'Politics'), ('travel', 'Travel'), ('food', 'Food'), ('music', 'Music'), ('movies', 'Movies'), ('games', 'Games'), ('books', 'Books'), ('art', 'Art'), ('animals', 'Animals'), ('other', 'Other')], default='other', max_length=255),
        ),
    ]