# django_vue
python3 django3 结合Vue.js框架构建前后端分离web开发

### Requirements

__Databases__: 

MySQL or PostgreSQL 11 or SQLite3

### Installation

Create virtual environment

`virtualenv -p python3 venv`

Activate virtual environment

`source ./venv/bin/activate`

Install dependencies

`pip install -r requirements.txt`

Uncomment in settings.py the connection setting required for 
your database, and change user and password accordingly

__Build front.__ Go to frontend folder and make production build

`npm run build`

or development build

`npm run dev`

__Note:__ some packages may need to be updated or additionally installed.
Read the npm response message and update/reinstall accordingly.

__Prepare backend.__ In project repository run

`python3 manage.py migrate`

and start server

`python3 manage.py runserver`
