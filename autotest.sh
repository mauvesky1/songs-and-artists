echo 'Hello from the best autotest.sh! Making this longer to do a push. Another test attempt going once, goin twice, going three times!
 Well, it needs to be tested again, and again!'

apt get install python3-pip3 python3-venv -y
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
pytest