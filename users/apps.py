from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
<<<<<<< HEAD

    def ready(self):
        import users.signals
=======
>>>>>>> a3d12e0c42f094e74ef03cbfbc1150cb0385b89a
