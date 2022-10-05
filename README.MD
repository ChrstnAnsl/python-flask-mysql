# Dental Records
---

## Prerequisite 

* Install latest xampp for windows
* Install python and pip
* VSCode
* Brew and MySQL for Mac

## TO DO

* Create env variable to auto-populate requirements.txt using pip shell (i think?)
* Fetch the userId of the user
* Create primary  key  for userId in the phpmyadmin

## APIs

* http://127.0.0.1:5000/users => GET
* http://127.0.0.1:5000/create_user => POST

## Debugging

* To find your chrome path use ./debug/chrome.ps1 in powershell

## Structure
* backend folder is for backend microservices and API
* frontend folder is for templates and UI
* templates folder is for rendering templates for testing purposes before the initial integration of front-end (this folder will be removed soon to prevent technical-debt)

## Running local env

* run python main.py
* using another terminal run ./local.sh to verify if the local environment is up and running
