# Standard Libs
import time
import os
import random
import string
import pyautogui

# Selenium Libs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



def getALine(file, num: int) -> str :
    for i in range(0, num-2) :
        file.readline()
    return file.readline()

class App :
    def __init__(self, numOfAccounts : int, listOfProxies : str) :
        self.nOA = numOfAccounts
        self.pr = listOfProxies
        self.diver = ""
        self.email = ""
        self.username = ""
        self.password = ""
        self.dOb = 0
        self.mOb = 0
        self.yOb = 0

    # Open The Browser And Go To Discord
    def VisitWeb(self) :
        os.system("nmcli g s")
        self.diver = webdriver.Firefox()
        self.diver.get("https://www.discord.com/register")        



    # Fill In Forms
    def FillInForm(self) :
        # Generate Random Values
        with open("usernames.txt", "r") as file :
            self.username = file.readlines()[random.randint(0, 81474)]
            self.email = self.username + ''.join(random.choice(string.digits) for _ in range(3)) + "@gmail.com"
            file.close()
        self.password = ''.join((random.choice(string.ascii_letters)) for _ in range(9))
        self.dOb = random.randint(1, 27)
        self.mOb = random.randint(1, 12)
        self.yOb = random.randint(1989, 1999)

        # Select Elements
        Username = self.diver.find_element(By.ID, "uid_7")
        Password = self.diver.find_element(By.ID, "uid_9")
        Email = self.diver.find_element(By.ID, "uid_5")
        DoB = self.diver.find_element(By.CLASS_NAME, "day-1uOKpp")
        MoB = self.diver.find_element(By.CLASS_NAME, "month-1Z2bRu")
        YoB = self.diver.find_element(By.CLASS_NAME, "year-3_SRuv")

        # Passing Values To Elements
        Username.send_keys(self.username)
        Password.send_keys(self.password)
        Email.send_keys(self.email)
        
        DoB.click()
        pyautogui.write(str(self.dOb), interval=0.5)
        pyautogui.hotkey('Enter')

        MoB.click()
        pyautogui.write(str(self.mOb), interval=0.4)
        pyautogui.hotkey('Enter')

        YoB.click()
        pyautogui.write(str(self.yOb), interval=0.6)
        pyautogui.hotkey('Enter')
    

    # Submit && Wait For User To Fill Captcha
    def finalFill(self) :
        Button = self.diver.find_element(By.CLASS_NAME, "button-1cRKG6")
        Button.click()
        for _ in range(10) :
            if self.diver.title.endswith("Friends") :
                break
            else :
                time.sleep(2)
                continue
    # Register And Store Token AlongSide Email
    # Store Username && Password && Email && Token


if __name__ == "__main__" :
    app = App(1, "")
    app.VisitWeb()
    app.FillInForm()
    app.finalFill()