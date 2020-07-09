class UptimeMonitor:

  def __init__(self, http_requests, ms_teams, gcloud_firestore):
    self.ms_teams = ms_teams
    self.gcloud_firestore = gcloud_firestore
    self.http_requests = http_requests

  def run(self):

    allwebsites = self.gcloud_firestore.get_document_dictionary('websites')
    if bool(allwebsites):
      status_document = 'websites_status'
      allwebsites_last_status = self.gcloud_firestore.get_document_dictionary(status_document)
      
      # To save the current website response status
      allwebsites_current_status = {}

      # Get the teams channel webhook
      settings = self.gcloud_firestore.get_document_dictionary('settings')

      for name, url in allwebsites.items():
        website_current_status = self.http_requests.get_status(url)
        
        allwebsites_current_status[name] = website_current_status

        if bool(allwebsites_last_status): # Were the status previously saved?
          if name in allwebsites_last_status: # Is this website previously checked?
            website_last_status = allwebsites_last_status[name]
            if website_current_status != website_last_status: # Website status has changed?
              if website_current_status >= 400:
                status_message = ' is down!'
              else:
                status_message = ' is up and running!'
              self.ms_teams.send_message(settings['teams_webhook'], f'{name} {status_message}', f'Status: {website_current_status}', url)
          else: # Is the first check
            status_message = f'Now monitoring with status: **{website_current_status}**'
            self.ms_teams.send_message(settings['teams_webhook'], name, status_message, url)

      # Save the current status for the next execution
      self.gcloud_firestore.save(status_document, allwebsites_current_status)