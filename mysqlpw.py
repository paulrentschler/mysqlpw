#!/usr/bin/env python

"""Command line script for creating MySQL users and changing user passwords.

   Use AT YOUR OWN RISK! Suggestions and improvements welcome.
   https://bitbucket.org/paulrentschler/mysqlpw

   Paul Rentschler <paul@rentschler.ws>
   """

import sys
import argparse
import getpass
import pyodbc


class MySQLpw(object):
    args = []


    def __init__(self):
        """Processes the command line arguments and stores the values provided.
           """
        parser = argparse.ArgumentParser()
        parser.add_argument(
            'user', 
            help="The MySQL user to create/change password for");
        self.args = parser.parse_args()

        self.changeUserPassword()


    def changeUserPassword(self):
        """Changes the user's (specified in args.user) password by asking for
           their current password then the new one (twice).
           """
        if self.args.user is not None and self.args.user != "":
            currentPw = getpass("Current password for "+self.args.user+": ")
            while True:
                newPw = getpass("New password: ")
                confirmPw = getpass("Confirm new password: ")

                if newPw != confirmPw:
                    print "Passwords did not match!\n\n";

                else:
                    print "Password changed.\n\n";
                    break

        else:
            print "ERROR: no user specified.\n\n";



if __name__ == '__main__':
    obj = MySQLpw()

