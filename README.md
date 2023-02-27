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

Initialize database (from root level):
`flask --app app_package init-db`

Run Flask server (from root level) w/ debug mode to allow auto-reloading :
`flask --app app_package run --debug`

To run test (from root level):
`python -m pytest`


To run test (from root level) w/ coverage:
`coverage run -m pytest`