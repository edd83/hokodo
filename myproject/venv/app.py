import os
import config
from flask import Flask
import requests
import json
import logging
from books import books
from authors import authors
from utils import json_to_array

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()

def fetch_data():
    uri = "https://hokodo-frontend-interview.netlify.com/data.json"
    try:
        url_response = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"
    json_response = url_response.text
    obj = json.loads(json_response)
    return obj['books']


def create_app():
  logger.info(f'Starting app in {config.APP_ENV} environment')
  app = Flask(__name__) 
  app.config.from_object('config')
  data = fetch_data()
  arr = json_to_array(data)

  @app.route('/books', methods=['GET'])
  def route_book():
    return books(data, arr)

  @app.route('/authors', methods=['GET'])
  def route_authors():
    return authors(arr)

  return app

if __name__ == "__app__":
   app = create_app()
   app.run(host='0.0.0.0', debug=True)