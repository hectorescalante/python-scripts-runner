def firestore_side_effect(self, document_path):
  if document_path == 'websites':
    return {
      'Google': 'http://www.google.com',
      'Amazon': 'http://www.amazon.com'
    }
  elif document_path == 'settings':
    return {
      'teams_webhook': 'http://www.teams.com/webhook'
    }
  elif document_path == 'websites_status':
    return {
      'Google': 200,
      'Amazon': 200
    }
  else:
    return {}

def testRun_WithStatusChange_ShouldSuccess(mocker):
  # Arrange
  from library.gcloud_firestore import GCloudFirestore
  mocker.patch.object(GCloudFirestore, '__init__', autospec=True)
  GCloudFirestore.__init__.return_value = None
  mocker.patch.object(GCloudFirestore, 'get_document_dictionary', autospec=True)
  GCloudFirestore.get_document_dictionary.side_effect = firestore_side_effect
  mocker.patch.object(GCloudFirestore, 'save', autospec=True)

  from library.http_requests import HttpRequests
  mocker.patch.object(HttpRequests, 'get_status', autospec=True)
  HttpRequests.get_status.return_value = 500

  from library.ms_teams import MsTeams
  mocker.patch.object(MsTeams, 'send_message', autospec=True)

  # Act
  from uptime_monitor import UptimeMonitor
  sut = UptimeMonitor(HttpRequests(), MsTeams(), GCloudFirestore(''))
  sut.run()

  # Assert
  assert HttpRequests.get_status.call_count == 2
  assert MsTeams.send_message.call_count == 2
