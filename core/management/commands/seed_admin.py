from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Cria um superusuário padrão se ele não existir'

    def handle(self, *args, **options):
        user = get_user_model()
        username = 'jcogfisica'
        email = 'jcogfisica@yahoo.com.br'
        password = 'MON010deo010'

        if not user.objects.filter(username = username).exists():
            user.objects.create_superuser(username = username, email = email, password = password)
            self.stdout.write(self.style.SUCCESS(f'Superusuário "{username}" criado com sucesso.'))
        else:
            self.stdout.write(self.style.WARNING(f'Superusuário "{username}" já existe.'))