import asyncore
import smtpd
import smtplib


class SimpleSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print("Receiving message from:", peer)
        print("Message addressed from:", mailfrom)
        print("Message addressed to:  ", rcpttos)
        print("Message length:        ", len(data))

        # Forward the email
        self.forward_email(mailfrom, rcpttos, data)
        return

    def forward_email(self, mailfrom, rcpttos, data):
        # SMTP settings for forwarding
        smtp_server = "SERVER"
        smtp_port = 587
        smtp_username = "USERNAME"
        smtp_password = "PASSWORD"

        # Create an SMTP client session object
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(smtp_username, smtp_password)
                server.sendmail(mailfrom, rcpttos, data)
            print("Email forwarded to", smtp_server)
        except Exception as e:
            print("Error: ", e)

        print("--------------------")


SimpleSMTPServer(("0.0.0.0", 8025), None)
print("Serving SMTP server on port 8025...")
asyncore.loop()
