import requests

class HttpRequests:

  def __init__(self):
    pass
  
  def get_status(self, url):
    try:
      response = requests.get(url)
      response_status = response.status_code
    except requests.RequestException:
      response_status = 404
    print (f'{url}: {str(response_status)}')
    return response_status