# Python jokes web support
This application represents support of random one line jokes for programmers (https://pyjok.es) shipped
with **_python_** and [_flask_](http://flask.palletsprojects.com) micro-web framework.

[![Build Status](https://travis-ci.org/vyahello/pyjokes-stand.svg?branch=master)](https://travis-ci.org/vyahello/pyjokes-stand)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/pyjokes-stand/badge.svg?branch=master)](https://coveralls.io/github/vyahello/pyjokes-stand?branch=master)

## Table of contents
- [Run application](#run-application)
- [Demo](#demo)
- [Run static code analysis](#run-static-code-analysis)
- [Contributing](#contributing)


### Run application
Run script from the root directory of the project:
```bash
python joker.py
```

### Demo
![Screenshot](static/img/demo.png)

### Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, `pydocstyle` and `unittests` (using `pytest`) accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-assessment.sh install-dependencies
```
Anyway it will be run via CI automatically after every change was made to the repo via Travis CI.

### Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.7+` is required to run the code
- `pip install -r requirements.txt` to install all project dependencies