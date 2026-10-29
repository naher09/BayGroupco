from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bay', '0014_fill_slugs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourconcernpagename',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, blank=True,
                                   help_text="Khali rakhle page name theke auto toiri hobe"),
        ),
        migrations.AlterField(
            model_name='partnerpagename',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, blank=True,
                                   help_text="Khali rakhle page name theke auto toiri hobe"),
        ),
    ]
