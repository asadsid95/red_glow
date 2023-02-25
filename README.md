To run app,

1. Create virtual environment at root level of folder
2. Install necessary packages
3. Run Flask server

----

For MacOS/Linux OS, create venv via:
`python3 -m venv venv`
OR
For Windows: create venv via:
`py -m venv venv`

Install necessary packages:
`pip install -r requirements.txt`

Run Flask server w/ debug mode to allow auto-reloading:
`flask --app app_package run --debug`