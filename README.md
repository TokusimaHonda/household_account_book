# household_account_book

## Python環境構築

```
ftakahashi-air@MacBookAir-FT household_account_book % python3 -m venv venv  
ftakahashi-air@MacBookAir-FT household_account_book % source venv/bin/activate
(venv) ftakahashi-air@MacBookAir-FT household_account_book % python -V 
Python 3.8.2
```

```
(venv) ftakahashi-air@MacBookAir-FT household_account_book % python -m pip install --upgrade pip 
Collecting pip
  Downloading https://files.pythonhosted.org/packages/ca/31/b88ef447d595963c01060998cb329251648acf4a067721b0452c45527eb8/pip-21.2.4-py3-none-any.whl (1.6MB)
     |████████████████████████████████| 1.6MB 4.8MB/s 
Installing collected packages: pip
  Found existing installation: pip 19.2.3
    Uninstalling pip-19.2.3:
      Successfully uninstalled pip-19.2.3
Successfully installed pip-21.2.4
(venv) ftakahashi-air@MacBookAir-FT household_account_book % python -m pip install Django==3.2.7  
Collecting Django==3.2.7
  Downloading Django-3.2.7-py3-none-any.whl (7.9 MB)
     |████████████████████████████████| 7.9 MB 4.5 MB/s 
Collecting pytz
  Using cached pytz-2021.1-py2.py3-none-any.whl (510 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     |████████████████████████████████| 42 kB 6.6 MB/s 
Collecting asgiref<4,>=3.3.2
  Using cached asgiref-3.4.1-py3-none-any.whl (25 kB)
Installing collected packages: sqlparse, pytz, asgiref, Django
Successfully installed Django-3.2.7 asgiref-3.4.1 pytz-2021.1 sqlparse-0.4.2
(venv) ftakahashi-air@MacBookAir-FT household_account_book % 
```


```
cd /Users/ftakahashi-air/work/Git/household_account_book
pip freeze > requirements.txt
pip install -r requirements.txt
```

## djangoコマンド


```
django-admin startproject household_account_book
python manage.py runserver
```