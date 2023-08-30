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
# You can update the announcements in the dashboard post widget.
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

# You can view the current data of the dashboard widget.
$ class-show-data -h
usage: class-show-data [-h] [-s | -a] [id] [max] [base_url]

positional arguments:
  id              Dashboard widget ID
  max             Maximum number of times to search in the event stream
  base_url        dashboard base_url default:https://classmario.fly.dev

optional arguments:
  -h, --help      show this help message and exit
  -s, --specific  outputs a SPECIFIC id value.
  -a, --all       shows all values. However, within the max value

$ class-show-data -s poster
{
  "text": "Stay hungry, stay foolish",
  "id": "poster",
  "updatedAt": 1693375461063
}

```

<img width="800" alt="image" src="https://github.com/edu-data-mario/classroom-notice-board-rest-clinet/assets/134017660/7a014960-f525-4eb0-ae64-90588e98d4d4">

```bash
$ class-write-team -h
usage: class-write-team [-h] [-a | -r] id label value [max] [base_url]

positional arguments:
  id           Dashboard TEAM widget ID - oneTeam|twoTeam|threeTeam
  label        Left value of row to be added to team widget
  value        Right value of the row to be added to the Team widget
  max          Maximum number of times to search in the event stream. default 10
  base_url     dashboard base_url default:https://classmario.fly.dev

optional arguments:
  -h, --help   show this help message and exit
  -a, --add    Adds a value to the Team widget.
  -r, --reset  Clears all values in the Team widget and registers only new values.

$ class-write-team -r oneTeam 홍길동 으샤으샤
$ class-write-team -r oneTeam 김좌진 "청산리 대첩을 승리"
$ class-write-team -a oneTeam 안중근 "히로부미를 저격"   
$ class-write-team -a oneTeam 윤봉길 "도시락 폭탄"    
$ class-write-team -a oneTeam 유관순 "3.1운동을 주도" 
$ class-write-team -a oneTeam 이봉창 "일왕을 암살 시도"    
$ class-write-team -a oneTeam 홍범도 "봉오동 전투를 승리"
$ class-write-team -r twoTeam 이완용 학부대신            
$ class-write-team -a twoTeam 이근택 군부대신
$ class-write-team -a twoTeam 이지용 내부대신 
$ class-write-team -a twoTeam 박제순 외부대신
$ class-write-team -a twoTeam 권중현 농상공부대신
$ class-write-team -r threeTeam 김좌진 "청산리 대첩의 영웅"
$ class-write-team -a threeTeam 홍범도 "대한독립군 총사령관"
$ class-write-team -a threeTeam 지청천 "만주군관학교 교장" 
$ class-write-team -a threeTeam 이범석 "만주군관학교 생도"
$ class-write-team -a threeTeam 이회영 "신흥무관학교 설립자"
```

<img width="800" alt="image" src="https://github.com/edu-data-mario/classroom-notice-board-rest-clinet/assets/134017660/94ed291a-8ce1-4f52-bae5-2cc4b151e8c5">

----

## Settings for Development
- Simple users don't have to read the part about the development environment below.

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
- https://pypi.org/project/Faker/ (Thank you, Jiyoung)