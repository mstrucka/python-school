import urllib.request
import datetime
from xml.dom import minidom
from fastapi import FastAPI
import json
import pandas

# done in class
def getHtml(website):
    fp = urllib.request.urlopen(website)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    with open("index.html", "w") as file:
        file.write(mystr)

# exercise 1, run uncommenting the main at the end of this file
def readJson():
    file = open("text.json")
    data = json.load(file)
    glossary = data['glossary']
    print(glossary['title'])


def readXml():
    xmldoc = minidom.parse("text.xml")
    print(xmldoc.firstChild.tagName)


def readTxt(fileName):
    with open(fileName, "r") as file:
        return file.read().strip()


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
    return json_file.to_json()

@app.get("/xml")
def get_xml():
    xml_file = pandas.read_xml("text.xml")
    return xml_file.to_json()

# if __name__ == '__main__':
    # exercise at class
    # getHtml("http://www.python.org")

    # exercise 1
    # readXml()
    # readJson()
    # readTxt()

    # exercise 2
