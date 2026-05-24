import os
import smtplib
from email.mime.text import MIMEText

# Lấy cấu hình từ két sắt bảo mật GitHub của bạn
EMAIL_NHAN = os.environ["EMAIL_NHAN"]
EMAIL_APP_PASSWORD = os.environ["EMAIL_APP_PASSWORD"]

def send_test_email():
    # Nội dung thư thử nghiệm
    msg = MIMEText("Két sắt GitHub và Mật khẩu ứng dụng Gmail của bạn đã hoạt động 100% rồi nhé!", _charset="utf-8")
    msg['Subject'] = '🔔 THỬ NGHIỆM: Bot GitHub gửi thư thành công!'
    msg['From'] = EMAIL_NHAN
    msg['To'] = EMAIL_NHAN

    try:
        # Kết nối đến server thư của Google
        with smtplib.SMTP_SSL('://gmail.com', 465) as server:
            server.login(EMAIL_NHAN, EMAIL_APP_PASSWORD)
            server.sendmail(EMAIL_NHAN, EMAIL_NHAN, msg.as_string())
        print("Gửi email thử nghiệm THÀNH CÔNG!")
    except Exception as e:
        print(f"Gửi email THẤT BẠI. Lỗi chi tiết: {str(e)}")

if __name__ == "__main__":
    send_test_email()
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
