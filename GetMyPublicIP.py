'''
Author: ZOUAHI Hafidh
This script should keep running on the distant machine.
'''

import requests
import re
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(message):
    msg = MIMEMultipart()
    password = "EMAIL_PASSWORD"      # Edit this line [Your e-mail password]
    msg['From'] = "EMAIL_ADDRESS"    # Edit this line [The e-mail address used to send the message]
    msg['To'] = "EMAIL_ADDRESS"      # Edit this line [The e-mail address where you would like to receive the message, can be the same as the
                                     #                 previous one]
    msg['Subject'] = "Public IP Address of your distant PC"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def main():
    ip = re.findall('\d+\.\d+\.\d+\.\d+', requests.post(url = 'https://whatismyipaddress.com/fr/mon-ip', headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}).text)[0]

    while True:
        try:
            old_ip = open('IP.txt').read().strip('\n')
            if old_ip != ip:
                send_mail('My Public IP address has changed! It is now: ' + ip)
        except FileNotFoundError:
            with open('IP.txt', 'w') as f: f.write(ip)
            send_mail('Hello! My IP Address is: ' + ip)
        time.sleep(300) # Wait 5 minutes, you can change this

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Process terminated by user.')
    except:
        print('An error has occured, please verify that you\'ve provided all the informations and try again.')


