import requests 
from bs4 import BeautifulSoup
import socket
from urllib.parse import urlparse


print("""        __________________________________________
           ____________________________________
            _________________________________
              _____________________________
               web sacraping with python
              _____________________________
            __________________________________
           _____________________________________
        ___________________________________________""")


class web_scarping:
    def elements(self, url, choice):
        response = requests.get(url)
        text = BeautifulSoup(response.text, "html.parser")
        title = text.title.string
        description = text.find_all('meta', attrs={'name': 'description'})
        if not description: description = "enable to locate description"
        else: 
          description = str(description[0])
          description = description.split("=")
          description = description[1].split("name")[0]
        parsed_url = urlparse(url)
        domain = parsed_url.hostname
        ip = socket.gethostbyname(domain)
        if choice == '1' : print(ip)
        if choice == '2' : print(description)
        if choice == '3' : print(title)
        if choice == '4' : print(text.html["lang"])
        if choice == '5' :
            print(f'\nip address is {ip}')
            print(f'\ntitel is {title}')
            print(f'\ndescription is {description}')
            print(f'\nlangauge is {text.html["lang"]}')

choice = input("[+]for ip address enter 1\n[+]for description enter 2\n[+]for title enter 3\n[+]for mother language enter 4\n[+]for all enter 5\n>")
url = input("please enter the url of target site`\n>")
if not choice or not url :
   print("you are not entred your choice or url, please try again! ")
run = web_scarping()
try:
  run.elements(url, choice)
except Exception as e :
    print(f"we detected a error {e}, please enter the correct name website try again!")