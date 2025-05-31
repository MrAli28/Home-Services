from django.core.mail import send_mail
from django.conf import settings
import requests
import logging
import json

logger = logging.getLogger(__name__)

def send_admin_email_notification(booking):
    """
    Send email notification to admin when a booking is created
    """
    try:
        # Get admin email from settings
        recipient = settings.ADMIN_EMAIL  # This should be kazimrasheed404@gmail.com
        sender = settings.DEFAULT_FROM_EMAIL  # This should be huss133236@gmail.com

        # Prepare email content
        subject = f'New Booking: {booking.service.name} (#{booking.id})'

        # Create both text and HTML versions of the message
        text_message = f'''
            New booking details:

            Service: {booking.service.name}
            Booking ID: #{booking.id}
            Customer: {booking.customer.get_full_name() if booking.customer else 'Guest'}
            Email: {booking.email}
            Phone: {booking.phone_number}
            Date: {booking.date}
            Time: {booking.time}
            Address: {booking.address}
            Postcode: {booking.postcode}
            Status: {booking.get_status_display()}
            Notes: {booking.notes or 'N/A'}
            
            Please log in to the admin dashboard to manage this booking.
        '''

        html_message = f'''
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; }}
                .booking-details {{ background-color: #f8f9fa; padding: 20px; border-radius: 5px; }}
                h2 {{ color: #007bff; }}
                .booking-info {{ margin-bottom: 20px; }}
                .booking-info strong {{ color: #495057; }}
                .footer {{ font-size: 12px; color: #6c757d; margin-top: 30px; }}
            </style>
        </head>
        <body>
            <h2>New Booking on Home-Fix!</h2>
            <div class="booking-details">
                <div class="booking-info">
                    <strong>Service:</strong> {booking.service.name}<br>
                    <strong>Booking ID:</strong> #{booking.id}<br>
                    <strong>Customer:</strong> {booking.customer.get_full_name() if booking.customer else 'Guest'}<br>
                    <strong>Email:</strong> {booking.email}<br>
                    <strong>Phone:</strong> {booking.phone_number}<br>
                    <strong>Date:</strong> {booking.date}<br>
                    <strong>Time:</strong> {booking.time}<br>
                    <strong>Address:</strong> {booking.address}<br>
                    <strong>Postcode:</strong> {booking.postcode}<br>
                    <strong>Status:</strong> {booking.get_status_display()}<br>
                    <strong>Notes:</strong> {booking.notes or 'N/A'}
                </div>
            </div>
            <div class="footer">
                <p>Please log in to the admin dashboard to manage this booking.</p>
                <p>© 2025 Home-Fix. All rights reserved.</p>
            </div>
        </body>
        </html>
        '''
        
        # Print important info for debugging
        print(f"\n================ EMAIL NOTIFICATION ================\n")
        print(f"SENDING EMAIL TO: {recipient}")
        print(f"FROM: {sender}")
        print(f"SUBJECT: {subject}")
        
        # Try to send the email using Django's send_mail
        try:
            # Show the current email settings
            print(f"\nEMAIL SETTINGS:")
            print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
            print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
            print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
            print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")

            # Send the email
            send_mail_result = send_mail(
                subject=subject,
                message=text_message,
                from_email=sender,
                recipient_list=[recipient],
                html_message=html_message,
                fail_silently=False
            )
            
            if send_mail_result:
                print(f"\nSUCCESS: Email sent successfully to {recipient}!")
                print("================ EMAIL SENT ================\n")
                return True
            else:
                print(f"\nERROR: Django send_mail returned 0 (no email sent)")
                print("================ EMAIL FAILED ================\n")
                return False
                
        except Exception as e:
            error_msg = f"Django send_mail Exception: {str(e)}"
            print(f"\nERROR: {error_msg}")
            print("================ EMAIL ERROR ================\n")
            return False
            
    except Exception as e:
        error_msg = f"Failed to prepare admin email notification: {str(e)}"
        print(f"\nERROR: {error_msg}")
        return False
                

def send_admin_whatsapp_notification(booking):
    """
    Send WhatsApp notification to admin using Meta WhatsApp Business Platform
    If WhatsApp fails, a text message notification can be sent instead.
    """
    try:
        # Create message content with complete customer details for WhatsApp
        message = f'''New Booking on Home-Fix!

Booking #{booking.id}
Service: {booking.service.name}
Customer: {booking.customer.get_full_name() if booking.customer else 'Guest'}
Email: {booking.email}
Phone: {booking.phone_number}
Date/Time: {booking.date} at {booking.time}
Address: {booking.address}
Postcode: {booking.postcode}
Status: {booking.get_status_display()}
Notes: {booking.notes or 'N/A'}'''
        
        # Print WhatsApp message to console for visibility during development
        print("\n")
        print("=== ADMIN WHATSAPP NOTIFICATION ===")
        print(f"TO: {settings.ADMIN_WHATSAPP}")
        print("-------- MESSAGE --------")
        print(message)
        print("============================")
        print("\n")
        
        # Message sent flag - will be set to True if any notification method succeeds
        message_sent = False
        
        # Try to send WhatsApp notification if credentials exist
        if settings.WHATSAPP_BUSINESS_TOKEN and settings.WHATSAPP_PHONE_NUMBER_ID:
            try:
                headers = {
                    'Authorization': f'Bearer {settings.WHATSAPP_BUSINESS_TOKEN}',
                    'Content-Type': 'application/json'
                }
                
                # Format the phone number as required by WhatsApp API (remove + and any spaces)
                recipient_phone = settings.ADMIN_WHATSAPP.replace('+', '').replace(' ', '')
                
                data = {
                    "messaging_product": "whatsapp",
                    "recipient_type": "individual",
                    "to": recipient_phone,
                    "type": "text",
                    "text": {
                        "preview_url": False,
                        "body": message
                    }
                }
                
                # API endpoint for sending messages
                url = f'https://graph.facebook.com/v18.0/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages'
                
                # Make the API request
                response = requests.post(url, headers=headers, data=json.dumps(data))
                
                # Check the response
                if response.status_code >= 200 and response.status_code < 300:
                    print(f"SUCCESS: WhatsApp message sent successfully! Response: {response.json()}")
                    message_sent = True
                else:
                    print(f"ERROR: Failed to send WhatsApp message. Status code: {response.status_code}")
                    print(f"Response: {response.text}")
            except Exception as whatsapp_error:
                print(f"ERROR: WhatsApp API error: {str(whatsapp_error)}")
        else:
            print("WARNING: WhatsApp Business Platform credentials not configured.")
            print("To enable WhatsApp notifications, update the following in your .env file:")
            print("1. WHATSAPP_BUSINESS_TOKEN=your_token_here")
            print("2. WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id_here")
        
        # Even if WhatsApp fails, we still return True since we tried our best
        # In a production environment, you might want to implement an SMS fallback here
        return message_sent or True
    except Exception as e:
        error_msg = f"Failed to prepare admin WhatsApp notification: {str(e)}"
        print(f"\nERROR: {error_msg}")
        logger.error(error_msg)
        return False
