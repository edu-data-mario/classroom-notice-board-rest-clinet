# classroom-notice-board-rest-clinet
- https://github.com/edu-data-mario/classroom-notice-board rest clinet

## USE
- import ↓
```bash
$ pip install classroom-notice-board-rest-clinet

$ python
Python 3.7.13 (default, Jul 13 2022, 10:21:28) 
[Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from classroom_notice_board_rest_clinet.restclient import update_poster
>>> update_poster(message="Stay hungry, stay foolish")
204
>>> 
```

- command line interface ↓
```bash
$ class-write-poster -h
usage: class-rest-client [-h] [-p | -t] msg [base_url]

positional arguments:
  msg           message
  base_url      dashboard base_url, default:https://classmario.fly.dev

optional arguments:
  -h, --help    show this help message and exit
  -p, --poster  updates the contents of the POSTER widget
  -t, --team    updates the contents of the TEAM widget
  
$ class-rest-client -p "Stay hungry, stay foolish"
SUCCESS UPDATE POSTER

$ class-show-data -s "poster"
{
  "text": "Stay hungry, stay foolish",
  "id": "poster",
  "updatedAt": 1693361875330
}

```

![image](https://github.com/edu-data-mario/classroom-notice-board-rest-clinet/assets/134017660/7a014960-f525-4eb0-ae64-90588e98d4d4)

----

## Settings for Development

### init
```bash
$ pdm init
Creating a pyproject.toml for PDM...
Please enter the Python interpreter to use
0. /Users/m2/.pyenv/shims/python3 (3.7)
1. /Users/m2/.pyenv/shims/python (3.7)
2. /Users/m2/.pyenv/shims/python3.11 (3.11)
3. /opt/homebrew/bin/python3.11 (3.11)
4. /Users/m2/.pyenv/versions/3.11.0/bin/python3.11 (3.11)
5. /Users/m2/.pyenv/shims/python3.10 (3.10)
6. /opt/homebrew/bin/python3.10 (3.10)
Please select (0):
Would you like to create a virtualenv with /Users/m2/.pyenv/versions/3.7.13/bin/python3? [y/n] (y):
Virtualenv is created successfully at /Users/m2/code/edu/classroom-notice-board-rest-clinet/.venv
Is the project a library that is installable?
If yes, we will need to ask a few more questions to include the project name and build backend [y/n] (n): y
Project name (classroom-notice-board-rest-clinet):
Project version (0.1.0):
Project description ():  https://github.com/edu-data-mario/classroom-notice-board rest clinet
Which build backend to use?
0. pdm-backend
1. setuptools
2. flit-core
3. hatchling
4. pdm-pep517
Please select (0):
License(SPDX name) (MIT):
Author name (dmario24):
Author email (becky2sawyer@gmail.com): data.mario24@gmail.com
Python requires('*' to allow any) (>=3.7):
Project is initialized successfully

$ ls -al
total 32
drwxr-xr-x  10 m2  staff   320  8 28 10:03 .
drwxr-xr-x   5 m2  staff   160  8 28 10:01 ..
-rw-r--r--   1 m2  staff  3102  8 22 11:26 .gitignore
-rw-r--r--   1 m2  staff    70  8 28 10:01 .pdm-python
drwxr-xr-x   6 m2  staff   192  8 28 10:01 .venv
-rw-r--r--   1 m2  staff    37  8 28 10:03 README.md
drwxr-xr-x   3 m2  staff    96  8 28 10:03 __pycache__
-rw-r--r--   1 m2  staff   393  8 28 10:03 pyproject.toml
drwxr-xr-x   3 m2  staff    96  8 28 10:03 src
drwxr-xr-x   4 m2  staff   128  8 28 10:03 tests

$ source .venv/bin/activate
(classroom-notice-board-rest-clinet-3.7) $  
```

### init test
```bash
$ pdm add --dev pytest
$ pytest
$ pytest -s
$ pytest tests/test_main.py::test_show_dashboard_data_all -s
```

### ref
- https://curlconverter.com/
- [curl guide by dashboard widget](https://github.com/Shopify/dashing/issues/56#issuecomment-11743170)
- [How to package a Python project to be run in the console](https://stackoverflow.com/questions/69638969/how-to-package-a-python-project-to-be-run-in-the-console)
- [파이썬 표준 라이브러리에서 권장하는 명령행 파싱 모듈인 argparse 에 대한 소개](https://docs.python.org/ko/3/howto/argparse.html#argparse-tutorial)
- https://stackoverflow.com/questions/38507593/dashing-get-value-from-a-widget-over-api