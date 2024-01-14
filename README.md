# FavoriteTunes
Simple Song playlist using Django
![Screenshot 2024-01-14 164800](https://github.com/Tushar-sahani/FavoriteTunes/assets/104075614/5df8f1e5-32b1-4830-9b82-f41408c8f8cf)

![Screenshot 2024-01-14 162927](https://github.com/Tushar-sahani/FavoriteTunes/assets/104075614/0f18191c-8203-4892-a2dd-5cc4650207f4)
## Installing


### Clone the project

```git
git clone https://github.com/Tushar-sahani/FavoriteTunes.git
```

### Install dependencies & activate venv

unix / mac

``` python
python3 -m pip install --user virtualenv
```

windows

```python
python -m pip install virtualenv
```

create a virtual environment

unix / mac

```python
python3 -m venv env
```

windows

```python
python -m venv env
```

And tell pip to install all of the packages in this file using the -r flag:

unix / mac

``` python
python3 -m pip install -r requirements.txt
```

windows

```python
python -m pip install -r requirements.txt
```


### Run the Project

Create Super user
```python
python manage.py createsuperuser
```
Enter Username And password to create super user

Now run this command:

``` python
python manage.py runserver
```
Go to Browser open Admin Panel
```terminal
http://127.0.0.1:8000/admin
```
Login with the Superuser (username and password) Add some Data into the Model (Artist and Songs)


Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view it in the browser.

