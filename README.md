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


## Installing pip

You will need pip to install the dependencies.

### on Debian/Ubuntu

    $ sudo apt-get install python-pip


### on RedHat/CentOS

    $ sudo yum install python-pip



## Dependencies

### **argparse** is used to parse the arguments passed via the command line

It can be installed via pip:

    $ sudo pip install argparse


### **MySQLdb** is used to connect to and talk to the MySQL database

Install it using:

#### on Debian/Ubuntu

    $ sudo apt-get install python-mysqldb

#### on RedHat/CentOS

    $ sudo yum install MySQL-python
