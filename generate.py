import requests
import random

class Person:
    def __init__(self):
        web = requests.get("https://randomuser.me/api/?nat=us") # Unites States, to prevent characters like Ö or ç from showing up.
        if not web.ok:
            print("[ERROR]  Failed requests")
            quit()
        else:
            web = web.json()['results'][0]
        self.username = web["login"]["username"]
        self.fname = web['name']['first']
        self.lname = web['name']['last']
        self.password = web["login"]['password'] + "_" + "".join([str(random.randint(0, 10)) for _ in range(4)])
    
    @property
    def name(self):
        return "%s %s" % (self.fname, self.lname)
    
    @name.setter
    def name(self, value):
        self.fname,self.lname=value.split(' ')
        
    @property
    def email(self):
        ending = random.choice(["gmail.com", "yahoo.com", "facebook.com", "peoplepc.com", "google.com"])
        return "%s.%s@%s" % (self.fname.lower(), self.lname.lower(), ending)
    
    @email.setter
    def email(self, value):
        self.fname,self.lname = value.split('@')[0].split(".")
