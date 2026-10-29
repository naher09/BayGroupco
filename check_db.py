from django.apps import apps
from django.db import connection

tables = connection.introspection.table_names()
with connection.cursor() as c:
    for m in apps.get_app_config('bay').get_models():
        t = m._meta.db_table
        if t not in tables:
            print("MISSING TABLE ", t)
            continue
        cols = {x.name for x in connection.introspection.get_table_description(c, t)}
        for f in m._meta.concrete_fields:
            if f.column not in cols:
                print("MISSING COLUMN", t, f.column)
print("check done")

