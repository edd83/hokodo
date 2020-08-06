from flask import request
import json
from utils import dict_to_json, is_desc
from datetime import datetime


def books_by_title(body, arr):
  sorted_books = sorted(arr, key=lambda x: (x['title']), reverse=is_desc(body['order']))
  return json.dumps(sorted_books, sort_keys=True, indent=4), 201

def books_by_published_date(body, arr):
  sorted_books = sorted(arr, key=lambda x: datetime.strptime(x['published'], '%Y-%m-%dT%H:%M:%S.%fZ'), reverse=is_desc(body['order']))
  return json.dumps(sorted_books, sort_keys=True, indent=4), 201

def books(data, arr):
  if request.json:
    body = dict_to_json(request.json)
    if body['type'] == 'date':
      return books_by_published_date(body, arr)
    elif body['type'] == 'title':
      return books_by_title(body, arr)
    else:
      return 'The type of the request is not recognise', 400
  else:
    return json.dumps(data, indent=4), 201