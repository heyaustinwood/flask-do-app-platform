# flask-do-app-platform
quickly setup and deploy a flask app to DigitalOcean app platform with GitHub integrations. Download this project and follow the steps below.

## setup flask project
1. download or fork the project
2. open terminal and cd into project folder
3. run following commands:
```
python3 -m venv venv
source venv/bin/activate
pip install flask
pip install -r requirements.txt
```
4. rename `.env.sample` to `.env`

## setup development database
1. setup local database named `doappplatform` or you can call it whatever you want, just make sure you change the `config.py` file to match. user: `postgres`, pass: `postgres`.

## test local app
1. run command in terminal: `python app.py`
2. add a faq, make sure local db connection works

## push to github
1. initialize project to your github account

## setup digital ocean app platform
1. go to digitalocean.com, login, and create a 
