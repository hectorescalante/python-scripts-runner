import json

class JsonFileStorage:

  def __init__(self, file_path):
    self.file_path = file_path
  
  def save(self, data):
    with open(self.file_path, 'w') as outputfile:
      json.dump(data, outputfile)

  def read(self):
    try:
      with open(self.file_path) as datafile:
        return json.load(datafile)
    except IOError as error:
      return {}
