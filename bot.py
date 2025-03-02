import os
import tweepy
from datetime import datetime

# Cargar Bearer Token desde el archivo .env
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Autenticación e instanciación de Tweepy
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Fin del mandato de Yamandú Orsi
finish_date = datetime(2030, 3, 1)

# Obtener fecha actual
today = datetime.now()
today = today.replace(hour=0, minute=0, second=0, microsecond=0)

# Obtener inicio del mandato
start_date = datetime(2025, 3, 1)

# Función para calcular los días restantes
def days_until():
    delta = finish_date - today
    return delta.days

# Función para calcular los días desde el comienzo
def days_since():
    delta = today - start_date
    return delta.days

# Función para calcular el porcentaje
def percentage_left(days_past):
    total = datetime(2030, 3, 1) - datetime(2025, 3, 1)
    return round(((days_past * 100) / total.days),2)

days_left = days_until()
days_past = days_since()
left = percentage_left(days_past)
tweet_text = f"Van {days_past} días de mandato de @OrsiYamandu. Ya pasó el {left}% de mandato."

# Función para enviar el tweet
def send_tweet(tweet_text):
    client.create_tweet(text=tweet_text)
    print("Tweet enviado correctamente.")

# Enviar el tweet
send_tweet(tweet_text)
