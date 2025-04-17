from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_bytes, force_str


def send_activation_email(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_link = f"http://localhost:8000/accounts/activate/{uid}/{token}/"

    subject = "Activation of the account in the Construction Management system"
    message = (
        f"Hi {user.first_name},\n\n"
        f"To set a password and activate your account, click the link below:\n\n"
        f"{activation_link}\n\n"
        f"If you have not created an account, ignore this message."
    )

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])