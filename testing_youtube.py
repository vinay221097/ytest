from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random 
import socket 
from webdriver_manager.chrome import ChromeDriverManager
import os,sys, stat
import subprocess
import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive',]


def upload_basic(img):
    """Insert new file.
    Returns : Id's of the file uploaded

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {'name': img,'parents': ['1BbfqfiKbAcgPGpNv0Au4tZsmiUmCxe0H']}
        media = MediaFileUpload(img,
                                mimetype='image/png')
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        # file = service.files().update( media_body=media,
        #                               fileId='1c7lRsb-sToy4_CsfcSH1m5Z4GYZtsIxr').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')



    

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)
options = Options()



print(subprocess.Popen("npm install get-firefox",shell=True,stdout=subprocess.PIPE).communicate()[0])
chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())

print(os.listdir(os.getcwd()+'/node_modules/get-firefox/lib'))
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')

path=r'chrome/chromedriver'
os.chmod(path, 0o777)
options = Options()
options.binary_location =binary_path
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
# vpn_path=os.getcwd()+"/chrome/vpn.crx"
# options.add_extension(vpn_path)
time.sleep(5)
# options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

# time.sleep(10)
# driver.get("chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html")
# time.sleep(3)

# print(driver.window_handles)
# if len(driver.window_handles)>1:
#     driver.switch_to.window(window_name=driver.window_handles[1])
#     driver.close()
# driver.switch_to.window(window_name=driver.window_handles[0])
# time.sleep(3)

# btn=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/button[2]").click()
# time.sleep(1)
# btn=driver.execute_script("return document.getElementsByClassName('select_location__button-box')[0].children[1].click()")
# vpn_count=driver.execute_script("return document.getElementsByClassName('locations')[0].childElementCount")
# random_vpn=random.randint(1,vpn_count)
# print(vpn_count,random_vpn)
# driver.execute_script("return document.getElementsByClassName('locations')[0].children[{}].click()".format(random_vpn))
# time.sleep(2)
# driver.save_screenshot("vpn.png")

# upload_basic("vpn.png")

# print("Your Computer Name2 is:" + hostname)    
# print("Your Computer IP Address2 is:" + IPAddr)
print(os.listdir(os.getcwd()))

print(os.listdir(os.getcwd()))
url = 'https://www.youtube.com/watch?v=in_mkPjpzqA'
path = 'scrape.png'


driver.get(url)
time.sleep(2)
cookies=[

    {'domain': '.youtube.com', 'expiry': 1696800781, 'httpOnly': True, 'name': 'LOGIN_INFO', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AFmmF2swRAIgeTSsxUyWhTidfq_qLwbF9J9PjopO7kk3EgLSwG2jdy4CIByzmM0oOgZ13nf_Eun1OkPxaLn3lnMeH1XCaleRY1Td:QUQ3MjNmelQzMDlFSDhjb3REVnp1bGtIN2l2WU1oX2NRRDIxRmNTZmttcnM4TTZueTR3cWlZcG1wT3JJMlNscjZvX3FzT2hla0F2Y3RjWkN4RkFHcm8xTm1iNzMySE82UG5ZekVUNkxiUkZyQXAxdWdxTnVxYnJRc3FySFZ5NlhSNGZlS2VfZVh6MmtuWXVyWWEzRFl0eE9PVmotNmh3N29n'}, 
    {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': 'SID', 'path': '/', 'secure': False, 'value': 'OAjcTQfQ3DWWajAPttwUu1MOMR7-HNujx33PIBs9iZ9qdOftXUuYBT0cDAAOqzLBXpEa5A.'}, 
    {'domain': '.youtube.com', 'expiry': 1696800756, 'httpOnly': False, 'name': 'CONSENT', 'path': '/', 'secure': True, 'value': 'PENDING+759'}, 
    {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'HSID', 'path': '/', 'secure': False, 'value': 'ALKicwGR6CrqSgocV'},
    {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'SSID', 'path': '/', 'secure': True, 'value': 'A9IY-7Y2ccQWGbw_W'},
    {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'SOCS', 'path': '/', 'secure': True, 'value': 'CAISEwgDEgk0NzEzNjQ0MzgaAmVuIAEaBgiAm9qYBg'}
    ]
for cookie in cookies:
    driver.add_cookie({'name':cookie['name'],'value':cookie['value']})
time.sleep(2)
driver.get(url)
time.sleep(2)

try:
    if driver.execute_script(" return document.getElementsByTagName('video')[0].paused")==True:
        actions = ActionChains(driver)
        actions.send_keys(Keys.SPACE).perform()
except:
    pass
duration= driver.execute_script(" return document.getElementsByTagName('video')[0].duration")
if duration is not None:
    duration=int(duration)
else:
    duration=random.randint(10,60)
random_duration=random.randint(duration-5,duration+5)
time.sleep(random_duration)

driver.save_screenshot(path)

upload_basic("scrape.png")

driver.quit()


