# DCS Archiving System

### Requirements:
* [Git](http://git-scm.com/downloads) _Download a native GUI client for ease of use_
* [Python](http://www.python.org/download/) _Get version 2.7.x_
* [Django](https://www.djangoproject.com/download/) _Get version 1.4.2_
* [MySQL](http://www.mysql.com/downloads/installer/)
* MySQL-Python - [Official (x86)](http://sourceforge.net/projects/mysql-python/) - [Unofficial (has x64)](http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python)
* [Python Image Library](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil) - Required by ImageField model
* [TWAINmodule] (http://www.lfd.uci.edu/~gohlke/pythonlibs/#twainmodule) - Required by scanner.py  _Deprecated_
* wxPython - [Official] (http://www.wxpython.org/download.php#stable) - [Unofficial (contains wxPython-common for Windows)] (http://www.lfd.uci.edu/~gohlke/pythonlibs/#wxpython) Required by scanner.py _Deprecated_



### Setting up the tools:
1. Install Git (Preferably using a native GUI client.)

2. Install Python.

3. To run python from command line, add installation directory (Eg. C:\Python27) to PATH: 

 1. Open My Computer > Right-Click > Properties > Advanced System Settings > Environment Variables
 2. Look for "Path" in "System Variables"
 3. Click "Edit" and APPEND directory (Eg. C:\Python27) to the end in Variable value: bla;bla;bla;C:\Python27
 4. Don't forget the ";" then Click Ok
 5. Restart any open Command Prompts
<br><br>
4. Install Django by: unzip the folder > open cmd > go to folder > type  "python setup.py install"

5. Install MySQL, MySQL-Python and Python Image Library

### Getting the Project
1. Clone [https://github.com/noelsison2/DCS-Archiving-System](https://github.com/noelsison2/DCS-Archiving-System)

2. Set up MySQL

 1. Open MySQL Workbench and click "Manage Security" under Server Administration
 2. Add two accounts (User@From host): CS192@localhost and CS192@127.0.0.1 both with "DB Manager" role enabled
 3. Add "New Connection" under SQL Development. User: CS192 Hostname: 127.0.0.1
<br><br>
2. Open _DCS-Archiving-System\DCSArchivingSystem_ in Command Prompt
3. Enter: python manage.py syncdb and python manage.py runserver
4. Open _127.0.0.1:8000_ in browser

### The Team:
* Carl Yu
* Noel Sison
* Marc Lopez
* Jasmine Tolentino
* Maricia Balayan
* John Smith Paraggua