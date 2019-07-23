import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com")
    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")
    return facts[0].getText()


def get_pig_latin_link(fact):
    payload = {'input_text': fact}
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/',
                             allow_redirects=False, data=payload)
    #print(f"response.headers: {response.headers}")
    #print(f"response.content: {response.content}")
    return response.headers['Location']


@app.route('/')
def home():
    fact = get_fact()
    dic = {"link": get_pig_latin_link(fact)}
    template = '<a href={link}>{link}</a>'
    return template.format(**dic)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

