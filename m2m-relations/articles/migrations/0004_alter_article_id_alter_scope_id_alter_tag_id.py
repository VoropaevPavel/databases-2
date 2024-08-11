from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_tag_scope_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scope',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]