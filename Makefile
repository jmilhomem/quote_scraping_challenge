VIRTUALENV_DIR=.env
PYTHON=${VIRTUALENV_DIR}/bin/python
PIP=${VIRTUALENV_DIR}/bin/pip
FILE_NAME="input-file.txt"


all:
        pip3 install virtualenv
        virtualenv -p python3 $(VIRTUALENV_DIR)
        $(PIP) install -r requirements.txt

run:
        python main.py

