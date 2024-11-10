import pyttsx3
import speech_recognition as sr
from flask import Flask, render_template
import pyaudio
from random import randrange
import collections
import random

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result",methods=['POST',"GET"])
    #output = request.form.to_dict()
    #name = output["name"]
def result():
    def speech_rec():
        r = sr.Recognizer()
        engine = pyttsx3.init()
        with sr.Microphone() as source:
            engine.say("your turn")
            engine.runAndWait()
            audio = r.listen(source)
        result1 = r.recognize_google(audio)
        return result1
    colours = ["red", "yellow", "blue", "brown", "orange", "green", "violet", "black", "pink"]
    import random
    engine = pyttsx3.init()
    mylist = list()
    comlist = list()
    for i in range(1, 50):
        if collections.Counter(comlist[:-1]) == collections.Counter(mylist):
            for z in range(5, 100, 4):
                print(z)
                choice = speech_rec()
                mylist = choice.split(" ")
                item = colours[randrange(len(colours))]
                if collections.Counter(mylist[:-1]) == collections.Counter(comlist) and choice != "" and item[
                                                                                                         :-1] != "":
                    comlist = mylist + [item]
                    print(mylist)
                    print(comlist)
                    engine.say("my turn")
                    engine.say(comlist)
                    engine.runAndWait()
                else:
                    engine.say("you lose")
                    engine.runAndWait()
                    break
        else:
            engine.say("you lose")
            engine.runAndWait()
            break
    #return  render_template("index.html",name=name)
if __name__ == '__main__':
    app.run(debug=True,port=5008)
