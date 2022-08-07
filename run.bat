@echo off
echo Hello!
echo If You're Running This App For The First Time, You'll Need Your Internet... 
echo Connection To Install Some Dependencies.
echo ......
echo Continue If YES
pause

pip3 install pipreqs
pip3 install pip-tools
pip3 install -r requirements.txt
python api.py
pause