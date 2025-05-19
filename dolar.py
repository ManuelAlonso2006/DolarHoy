import requests

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


def obtener_precios():
    url = 'https://criptoya.com/api/dolar'
    response = requests.get(url)
    data = response.json()
    mensaje = f"""{GREEN}🏦 Dolar Oficial: {data['oficial']['price']}{RESET}
{GREEN}💸 Dolar Ahorro: Vende: {data['ahorro']['bid']}, Compra: {data['ahorro']['ask']}{RESET}
{BLUE}💶 Dolar Blue: Vende: {data['blue']["bid"]}, Compra: {data['blue']["ask"]}{RESET}
{YELLOW}💳 Dolar Tarjeta: {data['tarjeta']['price']}{RESET}
{RED}💰 Dolar Mep: {data['mep']['al30']['ci']['price']}{RESET}
"""
    print(mensaje)


obtener_precios()