from django.db import migrations
from django.utils.text import slugify


def fill_slugs(apps, schema_editor):
    for model_name in ('OurConcernPageName', 'PartnerPageName'):
        Model = apps.get_model('bay', model_name)
        used = set()
        for obj in Model.objects.all().order_by('id'):
            base = (slugify(obj.page_name) or f"page-{obj.pk}")[:110]
            slug, i = base, 2
            while slug in used:
                slug = f"{base}-{i}"
                i += 1
            used.add(slug)
            Model.objects.filter(pk=obj.pk).update(slug=slug)


class Migration(migrations.Migration):

    dependencies = [
        ('bay', '0013_position_and_slug_add'),
    ]

    operations = [
        migrations.RunPython(fill_slugs, migrations.RunPython.noop),
    ]
