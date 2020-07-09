import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class GCloudFirestore:

  # Requires a configured GCloud Credential
  def __init__(self, root_path, gcp_project):
    self.credential = credentials.ApplicationDefault()
    firebase_admin.initialize_app(self.credential, {'projectId': gcp_project})
    self.client = firestore.client()
    self.root_path = root_path

  def get_document_dictionary(self, document_name):
    document_snapshot = self.client.document(f'{self.root_path}/{document_name}').get()
    if document_snapshot.exists:
      return document_snapshot.to_dict()
    else:
      return {}

  # data arg must be a dictionary
  def save(self, document_path, data):
    data_document = self.client.document(f'{self.root_path}/{document_path}')
    data_document.set(data)
