# Python-Keylogger
This is a simple Python Keylogger

## Modules Used
- python-xlib
- pynput
- logging

## Programming Language used
- python 2

## Description
Python keylogger is an application which is used to montor keyboard press and inputs.

## Module Installation Guide
Execute the following commands
```
sudo apt-get install  python-xlib
pip install pynput
```
##### logging module is pre-installed in python

## Steps to use it
- To make the script run on startup first go to your startup folder.
- Hold down the windows button and press “R” or type run in the windows menu to make the run dialog appear.
- Now type shell:startup in the dialog and press enter. This will open a window at your startup folder.
- Copy the keylogger into this folder and then create a new folder somewhere else for logs to be saved to. Make sure this folder is   not in the startup folder or it will be opened every time the computer has started. Open the keylogger in IDLE and now change the log_dir to the location of the folder you just created. Make sure this folder path uses forward slashes (‘/’) and contains a forward slash at the end.
- To stop the keylogger, open up task manager and look for anything named python as shown below due to windows just showing program names. If you have an older version of windows, I recommend looking for pythonw.exe. Right click on this and end the task.

## WARNING
This code is intended for educational purposes only.In no way do i endorse this script to be used for malicious purposes and i will not accept any responsibility for the running of this script.If you are going to test this keylogger on anyone , make sure they understand you are doing so.

## Author
- ***Jiten Sinha***-initial work-[LinekdIn](https://www.linkedin.com/in/jiten-sinha-131043159/)

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/jitensinha98/Python-Keylogger/blob/master/LICENSE) file for details.
