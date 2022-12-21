python3 -m venv create_any_filename  ===example===>python3 -m venv .venv 
 or 
python -m venv create_any_filename  ===example===>python -m venv .venv 


activate after creating 
=========================:

for wondows:
============
  create_any_filename\Scripts\activate.bat  ===> .venv\Scripts\activate.bat
  
for ubuntu:
===========
  source create_any_filename/bin/activate  ===>  .venv/bin/activate

 
 
 BEFORE INSTALLING 
  
  1)sudo apt install python3.8-venv
 
==============================================================================
===>To check the list of version of pip dependencies
pip list --format freeze

ref:
 https://note.nkmk.me/en/python-pip-list-freeze/
