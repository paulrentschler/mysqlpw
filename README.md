# MySQLpw - the missing password manager for MySQL

MySQLpw provides a secure way to create users and change passwords from the command line for a MySQL database.

All of the built-in MySQL ways of doing this will cause the new password to be logged in **plain-text** in either your .bashrc or .mysql_history file.


## Installation

To install the script, clone the repository and create a symlink for the executable into the appropriate bin directory.

    $ cd /usr/local
    $ sudo mkdir -p scripts/mysqlpw
    $ cd scripts/mysqlpw
    $ sudo hg clone https://bitbucket.org/paulrentschler/mysqlpw ./
    $ cd ../../bin
    $ sudo ln -s ../scripts/mysqlpw/mysqlpw.py ./


## Installing easy_install and/or pip

You will need easy_install or pip to install the dependencies. Pip is optional but it is the replacement for easy_install.

### on RedHat

  $ sudo yum install python-setuptools
  $ sudo easy_install pip



## Dependencies

### **argparse** is used to parse the arguments passed via the command line

It can be installed via easy_install or pip:

#### via easy_install

  $ sudo easy_install argparse

#### via pip

  $ sudo pip install argparse


### **MySQLdb** is used to connect to and talk to the MySQL database

It can be installed via apt-get, yum, easy_install, or pip:

#### via apt-get

  $ sudo apt-get install python-mysqldb

#### via yum

  $ sudo yum install MySQL-python

#### via easy_install

  $ sudo easy_install mysql-python

#### via pip

  $ sudo pip install mysql-python