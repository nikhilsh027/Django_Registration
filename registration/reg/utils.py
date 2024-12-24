# utils.py in your app directory
'''from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_registration_confirmation_email(email, user_name):
    """
    Send a registration confirmation email to the user
    """
    try:
        # Email subject
        subject = 'Welcome to Our Platform - Registration Confirmed'
        
        # Render HTML email template
        html_message = render_to_string('emails/registration_confirmation.html', {
            'user_name': user_name,
            'site_name': 'Registraion testing'
        })
        
        # Strip HTML to create plain text version
        plain_message = strip_tags(html_message)
        
        # Send email
        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception as e:
        # Log the error
        print(f"Email sending failed: {e}")
        return False'''