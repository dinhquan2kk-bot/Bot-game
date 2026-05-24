import os
import smtplib
from email.mime.text import MIMEText

EMAIL_NHAN = os.environ["EMAIL_NHAN"]
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]

def send_test_email():
    msg = MIMEText("Ket sat GitHub va Mat khau ung dung Gmail da hoat dong 100% roi nhe!", _charset="utf-8")
    msg['Subject'] = 'THU NGHIEM: Bot GitHub gui thu thanh cong!'
    msg['From'] = EMAIL_NHAN
    msg['To'] = EMAIL_NHAN

    try:
        with smtplib.SMTP_SSL('://gmail.com', 465) as server:
            server.login(EMAIL_NHAN, EMAIL_APP_PASSWORD)
            server.sendmail(EMAIL_NHAN, EMAIL_NHAN, msg.as_string())
        print("Gui email thu nghiem THANH CONG!")
    except Exception as e:
        print(f"Gui email THAT BAI. Loi chi tiet: {str(e)}")

if __name__ == "__main__":
    send_test_email()
