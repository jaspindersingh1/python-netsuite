import os
from netsuite.service import (client,
                              RecordRef,
                              ApplicationInfo,
                              Passport)

myRole = os.environ.get('ns_config.NS_ROLE')
myEmail = os.environ.get('ns_config.NS_EMAIL')
myPassword = os.environ.get('ns_config.NS_PASSWORD')
myAccount = os.environ.get('ns_config.NS_ACCOUNT')
myAppId = os.environ.get('ns_config.NS_APPID')

def make_passport():
    role = RecordRef(internalId=myRole)
    return Passport(email=myEmail,
                    password=myPassword,
                    account=myAccount,
                    role=role)


def login():
    app_info = ApplicationInfo(applicationId=myAppId)
    passport = make_passport()
    login = client.service.login(passport=passport,
                _soapheaders={'applicationInfo': app_info})

    print('Login Response: ', login.status)
    return client, app_info


passport = make_passport()
client, app_info = login()
