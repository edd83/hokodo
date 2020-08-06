import json

def authors(arr):
  result = []
  auths = []
  for book in arr:
    auths.append(book['author'])
  auths = list(dict.fromkeys(auths))
  for name in auths:
    obj = {"author": name, "books": list(filter(lambda x:name in x["author"],arr))}
    result.append(obj)
  return json.dumps(result, indent=4), 201
