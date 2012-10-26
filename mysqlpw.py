#!/usr/bin/env python

"""Command line script for creating MySQL users and changing user passwords.

   Use AT YOUR OWN RISK! Suggestions and improvements welcome.
   https://bitbucket.org/paulrentschler/mysqlpw

   Paul Rentschler <paul@rentschler.ws>
   """

import sys
import argparse
import getpass
import MySQLdb


class MySQLpw(object):
    args = []
    dbConnection = None


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
            currentPw = getpass.getpass("Current password for "+self.args.user+": ")
            while True:
                newPw = getpass.getpass("New password: ")
                confirmPw = getpass.getpass("Confirm new password: ")

                if newPw != confirmPw:
                    print "Passwords did not match!\n";

                else:
                    if not self.connectToDatabase(self.args.user, currentPw):
                        print "FAILED: could not connect to the database.\n";

                    else:
                        cursor = self.dbConnection.cursor()
                        cursor.execute("SET PASSWORD = PASSWORD(%s)", (newPw,))
                        cursor.close()
                        print "Password changed.\n";
                    
                    break

        else:
            print "ERROR: no user specified.\n";


    def connectToDatabase(self, user, password):
        """Establishes a connection to the local MySQL database.
           """
        try:
            self.dbConnection = MySQLdb.connect(
                host="localhost",
                user=user,
                passwd=password
                )
            return True

        except Exception, err:
            sys.stderr.write("ERROR: %s\n" % str(err))
            return False



if __name__ == '__main__':
    obj = MySQLpw()

