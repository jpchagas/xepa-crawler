from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    os.chdir(os.getcwd() + "/xepacrawler")
    os.system('scrapy crawl ceasars')
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
