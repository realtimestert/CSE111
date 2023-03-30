import random
import csv
from guizero import App, Text, PushButton, Picture
from datetime import datetime
import time

current_date_and_time = datetime.now(tz = None)

def main():
    app_window()

def app_window():
    
    # returns a random value from csv file and displays on the app window
    def change_message():
        message.value = random_magic()

    #return a random value from a txt file
    def change_message_2():
        message.value = (f"You {adjectives()} {nouns()}")     
    
    app = App(title="Staff of Chaos")
    message = Text(app, text = "Will you use the Staff of Chaos?")
    message2 = Text(app, align = "bottom", text = f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
    
    # Push the button to change the message
    button1 = PushButton(app, align = "left", text = "Use it", command = change_message)
    button2 = PushButton(app, align = "right", text = random_no_button(), command = change_message_2)

    #picture = Picture(app, align = "bottom", image="bearsgif.gif")
    
    app.display()

def random_magic():
    with open("10000_random.txt") as f:
        words = f.readlines()
        magic = random.choice(words)
    return magic

def random_no_button():
    with open("no.txt") as f:
        words = f.readlines()
        no = random.choice(words)
    return no

def random_no_press():
    with open("no_press.txt") as f:
        words = f.readlines()
        no_press = random.choice(words)
    return no_press

def adjectives():
    with open("adjectives.txt") as f:
        words = f.readlines()
        adjective = random.choice(words)
    return adjective

def nouns():
    with open("nouns.txt") as f:
        words = f.readlines()
        noun = random.choice(words)
    return noun

if __name__ == "__main__":
    main()