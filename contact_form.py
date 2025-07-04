# contact_form.py
import smtplib
from email.message import EmailMessage
import streamlit as st

def contact_form(name, email, message):
    try:
        smtp_user = st.secrets["mail"]["email"]
        smtp_password = st.secrets["mail"]["password"]

        msg = EmailMessage()
        msg['Subject'] = f"📬 New Message from {name}"
        msg['From'] = smtp_user
        msg['To'] = smtp_user
        msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        return True
    except Exception as e:
        print("❌ Email sending failed:", e)
        return False
