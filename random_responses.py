import random


def random_string():
    random_list = [
        "Please try writing something more descriptive. 🙂",
        "Oh! It appears you wrote something I don't understand yet😅",
        "Do you mind trying to rephrase that?😅",
        "I'm terribly sorry, I didn't quite catch that.🤔",
        "I can't answer that yet, please try asking something else.😐",
        "I'm really sorry, please pardon me but i'm still learning 😟", 
      "I'm sorry, i can't understand most things that people say, it's because i'm still immature and learning."
    ]

    
    return random.choice(random_list)