import os
import tweepy
from datetime import datetime

# Cargar Bearer Token desde el archivo .env
consumer_key = os.environ["CONSUMER_KEY_LUIS"]
consumer_secret = os.environ["CONSUMER_SECRET_LUIS"]
access_token = os.environ["ACCESS_TOKEN_LUIS"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET_LUIS"]

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

# Función para calcular los días restantes
def days_until():
    delta = finish_date - today
    return delta.days

days_left = days_until()
tweet_text = f"Falta{'n' if (days_left != 1) else ''} {days_left} días para que vuelva @LuisLacallePou."

# Función para enviar el tweet
def send_tweet(tweet_text):
    client.create_tweet(text=tweet_text)
    print("Tweet enviado correctamente.")

# Enviar el tweet
send_tweet(tweet_text)