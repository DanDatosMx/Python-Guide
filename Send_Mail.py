#Envío Masivo de Información desde un Excel
#Para enviar correos electrónicos masivos, puedes usar smtplib y openpyxl:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl

# Configuración del servidor de correo
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_user = 'tu_email@example.com'
smtp_password = 'tu_contraseña'

# Cargar datos desde Excel
wb = openpyxl.load_workbook('contactos.xlsx')
sheet = wb.active

# Enviar correos electrónicos
for row in sheet.iter_rows(min_row=2, values_only=True):
    nombre, email, mensaje = row

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = email
    msg['Subject'] = 'Asunto del correo'

    body = MIMEText(mensaje, 'plain')
    msg.attach(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, email, msg.as_string())

print("Correos enviados exitosamente.")
