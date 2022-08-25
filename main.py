import urllib.request
from xml.dom import minidom
import json


def getHtml(website):
    fp = urllib.request.urlopen(website)
    mybytes = fp.read()

    mystr = mybytes.decode("utf8")
    fp.close()
    with open("index.html", "w") as file:
        file.write(mystr)

def readJson():
    file = open("text.json")
    data = json.load(file)
    glossary = data['glossary']
    print(glossary['title'])


def readXml():
    xmldoc = minidom.parse("text.xml")
    print(xmldoc.firstChild.tagName)


def readTxt():
    with open("text.txt", "r") as file:
        print(file.read())


if __name__ == '__main__':
    # getHtml("http://www.python.org")
    readXml()
    readJson()
    readTxt()