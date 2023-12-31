# Generated by Django 4.2.7 on 2023-12-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Technology', 'technology'), ('Fashion', 'fashion'), ('Cars', 'cars'), ('Sports', 'sports'), ('Health', 'health'), ('Travel', 'travel'), ('Food', 'food'), ('Music', 'music'), ('Movies', 'movies'), ('Politics', 'politics'), ('Science', 'science'), ('Business', 'business'), ('Education', 'education'), ('Art', 'art'), ('Culture', 'culture'), ('Lifestyle', 'lifestyle'), ('Nature', 'nature'), ('Animals', 'animals'), ('History', 'history'), ('Photography', 'photography'), ('Design', 'design'), ('Books', 'books'), ('Gaming', 'gaming'), ('Other', 'other')], default='other', max_length=255),
            preserve_default=False,
        ),
    ]
