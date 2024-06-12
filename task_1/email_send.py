# 2 ta son uchun :  EKUK , EKUB


# pip install secure-smtplib
import smtplib, ssl

async def email_sender(user_email,message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "normffoster@gmail.com"  # Enter your address

    receiver_email = user_email # Enter receiver address
    password = "gysq nkux mpbs fmok"


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
