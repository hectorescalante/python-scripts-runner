def run_uptime_monitor(document_name):
  from tasks.uptime_monitor import UptimeMonitor
  from tasks.library.http_requests import HttpRequests
  from tasks.library.ms_teams import MsTeams
  from tasks.library.gcloud_firestore import GCloudFirestore

  monitor = UptimeMonitor(HttpRequests(), MsTeams(), GCloudFirestore(document_name, 'gcp-project-id') )
  monitor.run()

def main(task_name):
  print ('> Program start')
  
  # Website Uptime Monitor
  if task_name == 'uptime_monitor': run_uptime_monitor(task_name)
  
  print ('> Program end')

if __name__ == '__main__':
  import sys
  #sys.path.append(f'tasks')
  main(sys.argv[1])