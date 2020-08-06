import ast
import json

def dict_to_json(obj):
  return json.loads(json.dumps(obj))

def json_to_array(obj):
  return ast.literal_eval(json.dumps(obj))

# Ascendent by default
def is_desc(obj):
  return True if obj == 'desc' else False