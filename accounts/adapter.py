# accounts/adapter.py
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class FrontendAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        """
        Генерируем ссылку вида:
        https://your-frontend.com/confirm-email?key=<ключ>
        """
        key = emailconfirmation.key
        return f"{settings.FRONTEND_URL}/confirm-email?key={key}"
