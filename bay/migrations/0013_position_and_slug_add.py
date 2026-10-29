from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bay', '0012_alter_keymanagement_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourconcernpagename',
            name='position',
            field=models.PositiveIntegerField(default=0, help_text="Menu-te kon position-e dekhabe (choto number age ashbe)"),
        ),
        migrations.AddField(
            model_name='partnerpagename',
            name='position',
            field=models.PositiveIntegerField(default=0, help_text="Menu position (choto number age ashbe)"),
        ),
        migrations.AlterModelOptions(
            name='ourconcernpagename',
            options={'ordering': ['position', 'id']},
        ),
        migrations.AlterModelOptions(
            name='partnerpagename',
            options={'ordering': ['position', 'id']},
        ),
        migrations.AddField(
            model_name='ourconcernpagename',
            name='slug',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partnerpagename',
            name='slug',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
    ]
