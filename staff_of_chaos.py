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
        #message.value = (f"The staff speaks to you and says, {insults()}")
        message.value = insults()    
    
    # areas where the text appears on the app
    app = App(title="Staff of Chaos")
    message = Text(app, text = "Will you use the Staff of Chaos?")
    message2 = Text(app, align = "bottom", text = f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
    #message3 = Text(app, align = "bottom,", text = f"{pop_counted(button1)}")
    
    # ai generated image. Dream by Wombo
    picture = Picture(app, image = "the_staff.png")
    
    # Push the button to change the message
    button1 = PushButton(app, align = "left", text = "Use it", command = change_message)
    button2 = PushButton(app, align = "right", text = random_no_button(), command = change_message_2)

    #picture = Picture(app, align = "bottom", image="bearsgif.gif")
    
    app.display()

def random_magic():
    # small function to call a random phrase from a list
    with open("10000_random.txt") as f:
        words = f.readlines()
        magic = random.choice(words)
    return magic

def random_no_button():
    # small function to make the button text change each time the program is opened
    with open("no.txt") as f:
        words = f.readlines()
        no = random.choice(words)
    return no

def adjectives():
    # function to grab random adjectives
    with open("adjectives.txt") as f:
        words = f.readlines()
        adjective = random.choice(words)
    return adjective

def nouns():
    #function to grab random nouns
    with open("nouns.txt") as f:
        words = f.readlines()
        noun = random.choice(words)
    return noun

def insults():
    #combine a random adjective and a random noun to create an insult
    #for example, "uncultured swine"
    insult = adjectives() + nouns()
    return insult

def pop_counted(a):
    pop_counted.counter += 1
    return a.pop()
pop_counted.counter = 0

if __name__ == "__main__":
    main()