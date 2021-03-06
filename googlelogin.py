# Google Login
# From StackOverflow user: alexislg

from bs4 import BeautifulSoup
import requests

url_login = "https://accounts.google.com/ServiceLogin"
url_auth = "https://accounts.google.com/ServiceLoginAuth"

class GoogleSession:
    def __init__(self, login, pwd):
        global url_login, url_auth

        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content, "html.parser").find('form').find_all('input')
        login_creds = {}
        for u in soup_login:
            if u.has_attr('value'):
                login_creds[u['name']] = u['value']
        # override the inputs without login and pwd:
        login_creds['Email'] = login
        login_creds['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text
