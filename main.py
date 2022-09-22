import datetime
from xml.dom import minidom
from fastapi import FastAPI
import json
import pandas
import requests

# exercise 1, run uncommenting the main at the end of this file
def readJson():
    file = open("text.json")
    data = json.load(file)
    glossary = data['glossary']
    print('To showcase that I can find the title of this glossary, here it is:', glossary['title'])


def readXml():
    xmldoc = minidom.parse("text.xml")
    print('first tag to showcase I can play with it is:', xmldoc.firstChild.tagName)


def readTxt(filename):
    with open(filename, "r") as file:
        print(file.read().strip())
        file.close()

    with open(filename, "r") as file:
        return file.read()


app = FastAPI()

# exercise 2 , run via python -m uvicorn main:app --reload
@app.get("/")
def hello():
    return "Hello world!"


@app.get("/timestamp")
def timestamp():
    current_datetime = datetime.datetime.now().isoformat()
    return current_datetime

# exercise 2 continued, now using pandas library for everything except for the .txt, that is only retrieved
#  for the documentation, after the server is started, the API docs are to be found at 127.0.0.1:8080/docs


@app.get("/txt")
def get_txt():
    return readTxt("text.txt")


@app.get("/json")
def get_json():
    json_file = pandas.read_json("text.json")
    return json_file.to_string()


@app.get("/xml")
def get_xml():
    xml_file = pandas.read_xml("text.xml", xpath='//note')
    return xml_file.to_string()

# continuation of the date exercise, when the node is run, the timestamp from that server is retrieved here


@app.get("/js/timestamp")
def js_timestamp():
    response = requests.get('http://localhost:3000/timestamp')
    return response.text[1:-1]

# if __name__ == '__main__':
    # readXml()
    # readJson()
    # readTxt("text.txt")