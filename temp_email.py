import random
import requests
from os import path
from string import ascii_letters
from config import API, DOMAINES, create_dir
from validation import assert_bool, assert_mail, assert_str, assert_login
    
def create_email(login: str = None, domain: str = None) -> str:
    """ Create a new email account """
    if not login:
        login = generate_login()
    if not domain:
        domain = pick_domain()
    
    assert_login(login)
    assert_str(domain, has_int = True, has_special_char = True)
    mail = u'{0}@{1}'.format(login, domain)
    assert_mail(mail)
    
    requests.get(f"{API}?login={login}&domain={domain}")
    return mail

def check_mail(mail: str) -> None:
    assert_mail(mail)
    login, domain = mail.split('@')
    assert_login(login)
    assert_str(domain, has_int = True, has_special_char = True)
    
    request = requests.get(f'{API}?action=getMessages&login={login}&domain={domain}').json()
    assert_bool(len(request) > 0, True, "Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.")
    mails = []                          # This list will hold the mails ids fetched from the request
    for mail_id in request:
        for key, value in mail_id.items():
            if key == 'id':
                mails.append(value)
    
    mails_dir = create_dir(r'All Mails');
    for id in mails:
        request = requests.get(f'{API}?action=readMessage&login={login}&domain={domain}&id={id}').json()
        for key,value in request.items():
                if key == 'from':
                    sender = value
                if key == 'subject':
                    subject = value
                if key == 'date':
                    date = value
                if key == 'textBody':
                    content = value

        mail_files = path.join(mails_dir, f'{id}.txt')
        
        with open(mail_files, 'w') as file:
            file.write("Sender: " + sender + '\n' + "To: " + mail + '\n' + "Subject: " + subject + '\n' + "Date: " + date + '\n' + "Content: " + content + '\n')
    
def generate_login(length: int = 6) -> str:
    return ''.join(random.choice(ascii_letters) for _ in range(length))

def pick_domain() -> str:
    return random.choice(DOMAINES)
