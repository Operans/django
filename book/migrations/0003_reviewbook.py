# Generated by Django 4.2.6 on 2023-10-16 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_genre_book_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_review', models.TextField()),
                ('rate_stars', models.CharField(choices=[('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('title_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_object', to='book.book')),
            ],
        ),
    ]
