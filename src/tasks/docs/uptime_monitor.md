# Website Uptime Monitor

## Purpose
To notify a MS Teams channel when a Website change its response status.

## Description
Make GET calls to obtain the website http status and save it to compare with the next calls, if the status changed from the last call then send the notification.

## Data
Uses [Google Cloud Firestore Database](https://cloud.google.com/firestore) to save and retrieve the websites and its status, also the teams connector webhook is stored in the *settings* document.