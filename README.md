# Python jokes web support
> This application represents support of random one line jokes for programmers (https://pyjok.es) shipped
> with **_python_** and [_flask_](http://flask.palletsprojects.com) micro-web framework.
>
> Please follow https://pyjokes-stand.herokuapp.com web app to see how it looks like.

[![Build Status](https://travis-ci.org/vyahello/pyjokes-stand.svg?branch=master)](https://travis-ci.org/vyahello/pyjokes-stand)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/pyjokes-stand/badge.svg?branch=master)](https://coveralls.io/github/vyahello/pyjokes-stand?branch=master)

**Tools**
> - `pyjokes`
> - `python 3.7`
> - `html/css/js`
> - `pytest`
> - `shell`
> - `travis CI`
> - `heroku`


## Table of contents
- [Usage](#usage)
- [Development notes](#development-notes)

### Usage
Run script from the root directory of the project:
```bash
python joker.py
```

**Demo**
![Screenshot](static/img/demo.png)

### Development notes

#### Run static code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy`, `pydocstyle` and `unittests` (using `pytest`) accordingly.
To be able to start static code analysis _locally_ please run following script from the root directory of the project:
```bash
./run-code-assessment.sh install-dependencies
```
Anyway it will be run via CI automatically after every change was made to the repo via Travis CI.

#### Heroku deployment
Please follow instructions from - https://python-responder.org/en/latest/deployment.html

- Install heroku following by - https://devcenter.heroku.com/articles/heroku-cli#download-and-install
- Login to heroku
```bash
heroku login
```
- Create an application
```bash
heroku create pyjokes-stand
```
- Commit and push repo into a heroku
```bash
git add . && git commit -m "Add pyjokes heroku app" && git push heroku master
```
- Check heroku logs
```bash
heroku logs --tail
```
- Open an application via browser: https://pyjokes-stand.herokuapp.com

#### Meta
Heroku automation master – Volodymyr Yahello vyahello@gmail.com

Distributed under the `BSD` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at (for heroku automations inquiries):
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

#### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all project development dependencies
