import os
import pymsteams

class MsTeams:

  def __init__(self):
    pass

  def send_message(self, webhook, title, message, link):
    print(f'Teams Webhook: {webhook}')
    connectorcard = pymsteams.connectorcard(webhook)
    connectorcard.title(title)
    connectorcard.text(message)
    connectorcard.addLinkButton(link, link)
    print(f'|{title}| {message} [{link}]')
    connectorcard.send()