### django-admin
```
django-admin startproject serverless_django .
```

### create sqlite database
```
python3 manage.py migrate
```
```
bharathkumarraju@R77-NB193 2.Django % python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
bharathkumarraju@R77-NB193 2.Django % 
```

### create sqlite database for another prod settings module which creates prod.sqlite3
```
python3 manage.py migrate --settings serverless_django.prod_settings
```

### Use environment variables
```
DJANGO_SETTINGS_MODULE=serverless_django.settings.production python3 manage.py migrate
```

### run both local and prod
```
DJANGO_SETTINGS_MODULE=serverless_django.settings.production python3 manage.py migrate
```

### pages

```
python3 manage.py startapp pages
```

### run server local
```
 python3 manage.py runserver
```

### run server prod

```
python3 manage.py migrate --settings serverless_django.settings.production
python3 manage.py runserver --settings serverless_django.settings.production
```