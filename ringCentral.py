# https://developers.ringcentral.com/my-account.html#/applications
# Find your credentials at the above url, set them as environment variables, or enter them below
import os
from ringcentral import SDK

class CreateExtension:
    def __init__(self):

        # PATH PARAMETERS
        self.accountId = '~'
        self.rcsdk = SDK(os.environ['clientId'], os.environ['clientSecret'], os.environ['serverURL'])
        self.platform = self.rcsdk.platform()
        self.body = {
            'contact': {
                'firstName': '<ENTER VALUE>',
                'lastName': '<ENTER VALUE>',
                'email': '<ENTER VALUE>',
                'businessPhone': '',
                'mobilePhone': '<ENTER VALUE>',

                'emailAsLoginName': True,
                'pronouncedName': {
                    'type': 'Default',
                    'text': ''
                },
                'department': ''
            },
            'extensionNumber': '<ENTER VALUE>',
            'password': 'D3f4ultP@ss',
            'references': [],

            'setupWizardState': 'NotStarted',
            'status': 'Enabled',
            'type': 'User',
            'hidden': False
        }

    def login(self):
        self.platform.login(os.environ['username'], os.environ['extension'], os.environ['password'])

    def getBody(self):
        return self.body

    def send(self):
        self.response = self.platform.post(f'/restapi/v1.0/account/{self.accountId}/extension', self.body)
        return self.response

    def setContact(self, firstname, lastname, email, mobile=''):
        self.body['contact']['firstName'] = str(firstname)
        self.body['contact']['lastName'] = str(lastname)
        self.body['contact']['email'] = str(email)
        self.body['contact']['mobilePhone'] = str(mobile)


    def setExtension(self, ext):
        self.body['extensionNumber'] = str(ext)

    def overrideDefaultPassword(self, password):
        self.body['password'] = str(password)


