import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import pytz
import time


def obtener_precios():
    url = 'https://criptoya.com/api/dolar'
    response = requests.get(url)
    data = response.json()
    return data

def enviar_mail(data):
        correo_origen = "example@gmail.com"
        contraseña = "xxxx xxxx xxxx xxxx"
        correo_destino = 'tucorreo@gmail.com'
        asunto = 'Dolar Hoy'
        mensaje = f"""
            Dolar Blue: {data['blue']["ask"]}
            Dolar Oficial: {data['oficial']['price']}
            Dolar Mep: {data['mep']['al30']['24hs']['price']}
            Dolar Tarjeta: {data['tarjeta']['price']}
        """
        try:
            # Crear el mensaje
            msg = MIMEMultipart()
            msg['From'] = correo_origen
            msg['To'] = correo_destino
            msg['Subject'] = asunto
            msg.attach(MIMEText(mensaje, 'plain'))
            # Conexión con el servidor SMTP de Gmail
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()  # Usar conexión segura
            servidor.login(correo_origen, contraseña)
            servidor.send_message(msg)
            servidor.quit()
        except Exception:
            return f"Ah ocurrido un error al enviar el correo"
        
        
def tarea():
    argentina = pytz.timezone("America/Argentina/Buenos_Aires")
    ahora = datetime.now(argentina)
    if ahora.strftime("%H:%M") == "05:00" or ahora.strftime("%H:%M") == "17:00":
        enviar_mail(obtener_precios())
        
while True:
    tarea()
    time.sleep(60)