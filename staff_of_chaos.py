import random
import csv
from guizero import App, Text, PushButton

def main():
    app_window()

def app_window():
    
    # returns a random value from csv file and displays on the app window
    def change_message():
        message.value = random_magic()

    #return a random value from a txt file
    def change_message_2():
        message.value = "The staff makes fun of you."      
    
    app = App(title="Staff of Chaos")
    message = Text(app, text = "Will you use the Staff of Chaos?")
    
    # Push the button to change the message
    button1 = PushButton(app, align = "left", text = "Use it", command = change_message)
    button2 = PushButton(app, align = "right", text = random_no(), command = change_message_2)
    
    app.display()

def random_magic():
    with open("10000_random.txt") as f:
        words = f.readlines()
        magic = random.choice(words)
    return magic

def random_no():
    with open("no.txt") as f:
        words = f.readlines()
        no = random.choice(words)
    return no

if __name__ == "__main__":
    main()