from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time
import os
from pystyle import *
from InquirerPy import inquirer
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains

verboose = False
banner = '''
________    _________.____ ____   ____ ___________.__                               
\______ \  /   _____/|    |\   \ /   / \__    ___/|  |__   ____  ___________ ___.__.
 |    |  \ \_____  \ |    | \   Y   /    |    |   |  |  \_/ __ \/  _ \_  __ <   |  |
 |    `   \/        \|    |__\     /     |    |   |   Y  \  ___(  <_> )  | \/\___  |
/_______  /_______  /|_______ \___/      |____|   |___|  /\___  >____/|__|   / ____|
        \/        \/         \/                        \/     \/             \/     
                  
                          Made by: @DaniDuese#4798
                          
                          
'''

# check whic os is used and set clear command
if os.name == "nt":
    clear = "cls"
else:
    clear = "clear"

os.system(clear)
print(Colorate.Vertical(Colors.blue_to_green, banner,2))
course = inquirer.select(
    message="Which Certificate would you like to get:",
    choices={
        "Ski Level 1": None,
        "Ski Level 2": None,
        "Ski Level 3": None,
        "Snowboard Level 1": None,
        "Snowboard Level 2": None,
        "Snowboard Level 3": None,
        "Nordic Level 1": None,
        "Nordic Level 2": None,
        "Nordic Level 3": None,
        "Telemark Level 1": None,
        "Telemark Level 2": None,
    },
).execute()
browser = inquirer.select(message="Which browser would you like to use?", choices={"Safari": None, "Chrome": None, "Edge": None}).execute()
verboose = inquirer.confirm(message="Verboose? [Shows the debugging messages]").execute()
fillform = inquirer.confirm(message="Auto fill Form? [Automatically fills the form with the data you entered]").execute()
if fillform == True:
    name = inquirer.text(message="Enter your full name:").execute()
    birthdate = inquirer.text(message="Enter your birthdate: [YEAR-MONTH-DAY]").execute()
    email = inquirer.text(message="Email Adress:").execute()

if browser == "Chrome":
    driver = webdriver.Chrome()
elif browser == "Edge":
    driver = webdriver.Edge()
elif browser == "Safari":
    driver = webdriver.Safari()
else:
    print("Browser not supported!")
    exit()
driver.get("https://www.dslv-theorie.de")
driver.implicitly_wait(0.5)
#click on next button (/html/body/div[2]/div/div/div/div/div[1]/div/button)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[1]/div/button').click()
driver.implicitly_wait(0.5)
# click on next button (/html/body/div[2]/div/div/div/div/div[2]/div/button)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/div/button').click()
driver.implicitly_wait(0.5)
# click on next button (/html/body/div[2]/div/div/div/div/div[3]/div/div/button[1])
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/div/div/button[1]').click()
# click button
if course == "Ski Level 1":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div/div[2]/div/a/div').click() 
    with open('jsons/level-1-ski.json') as f:
        data = json.load(f)
elif course == "Ski Level 2":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[3]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-2-ski.json') as f:
        data = json.load(f)
elif course == "Ski Level 3":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[4]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-3-ski.json') as f:
        data = json.load(f)
elif course == "Snowboard Level 1":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[5]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-1-snowboard.json') as f:
        data = json.load(f)
elif course == "Snowboard Level 2":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[6]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-2-snowboard.json') as f:
        data = json.load(f)
elif course == "Snowboard Level 3":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[7]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-3-snowboard.json') as f:
        data = json.load(f)
elif course == "Nordic Level 1":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[8]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-1-nordic.json') as f:
        data = json.load(f)
elif course == "Nordic Level 2":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[9]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-2-nordic.json') as f:
        data = json.load(f)
elif course == "Nordic Level 3":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[10]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-3-nordic.json') as f:
        data = json.load(f)
elif course == "Telemark Level 1":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[11]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-1-telemark.json') as f:
        data = json.load(f)
elif course == "Telemark Level 2":
    driver.find_element(
    By.XPATH, '//*[@id="app"]/main/div/div/div[12]/div/div/div[2]/div/a/div').click()
    with open('jsons/level-2-telemark.json') as f:
        data = json.load(f)
else:
    quit()

def AnswerQuestion():
    question2 = driver.find_element(By.CLASS_NAME, "md-title")
    answer1 = driver.find_element(
        By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[2]/ul/label[1]/li/div/div[1]')
    answer2 = driver.find_element(
        By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[2]/ul/label[2]/li/div/div[1]')
    answer3 = driver.find_element(
        By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[2]/ul/label[3]/li/div/div[1]')
    question3 = question2.text
    question3 = question3.strip()
    # find the answer for the question in the json file
    for i in data:
        # check if i['question'] is part of question3
        if question3 in i['question'] or i['question'] in question3 or question3 == i['question']:
            if verboose == True:
                print("Question: ",i['question'])
            for j in i['answers']:
                if j['is_correct'] == True:
                    answer = j['answer']
                    if verboose == True:
                        print("Question Number: ",i)
                    if answer in answer1.text:
                        if verboose == True:
                            print("Answer 1 is correct")
                        try :
                            driver.find_element(
                                By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[2]/ul/label[1]/li/div').click()
                        except WebDriverException:
                            pass
                            break
                    elif answer in answer2.text:
                        if verboose == True:
                            print("Answer 2 is correct")
                        try:
                            driver.find_element(
                                By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[2]/ul/label[2]/li/div').click()
                        except WebDriverException:
                            pass
                            break
                    elif answer in answer3.text:
                        if verboose == True:
                            print("Answer 3 is correct")
                        try:
                            driver.find_element(
                                By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[2]/ul/label[3]/li/div').click()
                        except WebDriverException:
                            break
                    else:
                        print("No answer found")
                        
    


for i in range(0, 500):
    AnswerQuestion()
    print(i)
    try:
        driver.implicitly_wait(0.2)
        driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/form/div/div[3]/button[2]/div/div').click()
        driver.implicitly_wait(0.2)
        driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/div/div[3]/button/div').click()
        driver.implicitly_wait(0.2)
    except WebDriverException:
        break

if fillform == True:
    if verboose == True:
        print("Filling out Form")
    try:
        nameinput = driver.find_element(By.ID, 'name')
        nameinput.send_keys(name)
        # press tab
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(birthdate)
        actions.send_keys(Keys.TAB)
        actions.send_keys(email)
        actions.perform()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/form/button').click()
    except WebDriverException:
        print("Error while filling out the form")
        pass

time.sleep(30)

quit()
