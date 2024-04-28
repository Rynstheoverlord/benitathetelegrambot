from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import json, random

with open("bot.json", 'r') as ds:
  training_data = json.load(ds)

  greeting_training_data = training_data["greeting_training_data"]

greeting_data_replies = training_data["greeting_data_replies"]

def get_message(message):
  blob = TextBlob(message)
  sentiment = blob.correct().sentiment.polarity
  cl = NaiveBayesClassifier(greeting_training_data)
  if cl.classify(message) == "greeting":
    return random.choice(greeting_data_replies)