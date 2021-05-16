# Generated by Django 3.2.2 on 2021-05-16 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, verbose_name='Вопрос')),
                ('sequence', models.PositiveSmallIntegerField(verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Набор',
                'verbose_name_plural': 'Наборы Тестов',
            },
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_true_answer', models.BooleanField(default=False, verbose_name='Правильность Ответа')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cart', verbose_name='Карточка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.set', verbose_name='Набор'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Текст')),
                ('is_true', models.BooleanField(default=False, verbose_name='Верный')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cart', verbose_name='Карточка')),
            ],
            options={
                'verbose_name': 'Вариант Ответа',
                'verbose_name_plural': 'Варианты Ответов',
            },
        ),
    ]
