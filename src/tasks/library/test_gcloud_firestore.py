def testGetDocumentDictionary_WithEmptyDocumentName_ShouldSuccess(mocker):
  # Arrange
  import firebase_admin
  mocker.patch.object(firebase_admin, 'initialize_app', autospec=True)

  from firebase_admin import credentials
  mocker.patch.object(credentials, 'ApplicationDefault', autospec=True)

  from firebase_admin import firestore
  mocker.patch.object(firestore, 'client', autospec=True)

  # Act
  from gcloud_firestore import GCloudFirestore
  sut = GCloudFirestore('')
  result = sut.get_document_dictionary('')

  # Assert
  #TODO: