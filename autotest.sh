apt get install python3-pip3 python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
pytest --cov-report term-missing --cov=application tests/