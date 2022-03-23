import sys
import os
from ringCentral import CreateExtension

# Sandbox Credentials

os.environ['clientId'] = '3MN2yPqjTLWEWLQGur4Lww'
os.environ['clientSecret'] = 'rr7KCnmpSKiNFIo82daQiAYLB78x0-Qo-kseW_M_OwTg'
os.environ['serverURL'] = 'https://platform.devtest.ringcentral.com'
os.environ['username'] = '+14372539073'
os.environ['extension'] = '101'
os.environ['password'] = 'adm1nP@ss4RING'

# Object Creation and Usage
account = CreateExtension()

try:
    fname = sys.argv[1]
except IndexError:
    fname = input("Enter the User's First Name: ")

try:
    lname = sys.argv[2]
except IndexError:
    lname = input("Enter the User's Last Name: ")

try:
    emailadd = sys.argv[3]
except IndexError:
    emailadd = input("Enter the User's Email Address: ")

try:
    ext = sys.argv[4]
except IndexError:
    ext = input("Enter the User's Extension: ")


account.setContact(fname, lname, emailadd)
account.setExtension(ext)
account.login()
print(account.send())

print(account.getBody())
