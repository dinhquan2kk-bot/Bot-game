import os
import time
import smtplib
from email.mime.text import MIMEText
from playwright.sync_api import sync_playwright

EMAIL_NHAN = os.environ["EMAIL_NHAN"]
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]
GAME_USERNAME = os.environ["GAME_USERNAME"]
GAME_PASSWORD = os.environ["GAME_PASSWORD"]

def send_to_email(content):
    msg = MIMEText(content, _charset="utf-8")
    msg['Subject'] = '🔵 Cap nhat du lieu Mystera Legacy'
    msg['From'] = EMAIL_NHAN
    msg['To'] = EMAIL_NHAN
    try:
        with smtplib.SMTP_SSL('://gmail.com', 465) as server:
            server.login(EMAIL_NHAN, EMAIL_APP_PASSWORD)
            server.sendmail(EMAIL_NHAN, EMAIL_NHAN, msg.as_string())
        print("Da gui email thanh cong!")
    except Exception as e:
        print("Loi khi gui email:", e)

def get_game_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("https://mysteralegacy.com")
            page.wait_for_load_state("networkidle")
            
            # Tu dong dien tai khoan va mat khau game từ két sắt bảo mật
            page.fill("#username_input_field", GAME_USERNAME) 
            page.fill("#password_input_field", GAME_PASSWORD)
            page.click("#login_button")
            time.sleep(5)
            
            # Lenh doc du lieu tu man hinh game mang ve
            du_lieu = page.evaluate("""() => {
                let level = document.querySelector('.player-level-class')?.innerText || "Chua ro";
                return `He thong chay ngam on dinh. Cap do nhan vat hien tai: ${level}`;
            }""")
            return du_lieu
        except Exception as e:
            return f"Khong ket noi duoc vao game: {str(e)}"
        finally:
            browser.close()

if __name__ == "__main__":
    ket_qua_game = get_game_data()
    send_to_email(ket_qua_game)
