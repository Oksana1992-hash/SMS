import smtplib
from email.message import EmailMessage

sender_email = 'oksana1992h@yandex.ru'
recipient_email = 'oksana1992python@yandex.ru'
password = 'xwfxdjnnwjvamwtr' #Это пароль приложения! Не ящика!
subject = 'Проверка связи №1'
body = 'Привет №1 из Питона!'

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

server = None

try:
    # Использование порта 465 для SSL
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print('Письмо отправлено!')
except Exception as e:
    print(f'Ошибка: {e}')
finally:
    if server:
        server.quit()
