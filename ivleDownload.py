# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, os, time

# Set user-defined variables
folder = "folderpath" # where we should download the files
username = "username" # IVLE username
password = "password" # IVLE password

# Set required variables
#urlHead = "https://ivle.nus.edu.sg/v1/"
headers = {
"User-Agent":
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

s = requests.session() # for file downloads
s.headers.update(headers)

driver = webdriver.Chrome("chromedriver.exe") # for navigating. we use selenium as we need the javascript to load the file directory on IVLE
driver.get("https://ivle.nus.edu.sg/")
userInput = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_userid")
userInput.send_keys(username)
pwInput = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_password")
pwInput.send_keys(password)
pwInput.send_keys(Keys.ENTER)
for cookie in driver.get_cookies(): # update requests with 
    c = {cookie['name']: cookie['value']}
    s.cookies.update(c)

os.chdir(folder) # for saving files

links = []
files = []

def fetchItems(itemDict):
    print(itemDict["path"])
    driver.get(itemDict["link"])
    
    # Wait for the page to load
    time.sleep(0.5)
    tryAgain = True
    while tryAgain:
        tryAgain = False
        try:
            driver.find_element_by_id("mainTable").find_element_by_css_selector("tbody")
        except:
            tryAgain = True
            time.sleep(0.5)
    
    # Search for the files/folders
    for item in driver.find_element_by_id("mainTable").find_element_by_css_selector("tbody").find_elements_by_css_selector("tr"):
        try:
            name = item.find_element_by_css_selector("a")
            icon = item.find_element_by_css_selector("img").get_property("src")
        except:
            continue
        if "folder" in icon:
            if icon == "https://ivle.nus.edu.sg/v1/content/images/foldericon/folder_full.png":
                # open it
                links.append({"path": itemDict["path"] + "/" + name.text.replace("/", "_"), "link": name.get_property("href")})
        else:
            # Create the directory if it doesn't exist
            if not os.path.exists(itemDict["path"]):
                os.makedirs(itemDict["path"])
            # Check if the file exists
            if not os.path.isfile(itemDict["path"]+"/"+name.text.replace("/", "_")):
                files.append({"path": itemDict["path"]+"/"+name.text.replace("/", "_"), "link": name.get_property("href")})
                
    while links:
        fetchItems(links.pop(0))
    while files:
        fileDict = files.pop(0)
        print("Downloading", fileDict["path"])
        r = s.get(fileDict["link"])
        with open(fileDict["path"], "wb") as f:
            for block in r.iter_content(1024):
                f.write(block)

modsPanel = driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolder1_pnlStudentModules").find_element_by_class_name("panel-body")
for panel in modsPanel.find_elements_by_class_name("panel-heading"):
    mod = panel.find_element_by_class_name("col-md-7").find_element_by_css_selector("a")
    modName = mod.text.replace("/", "_")
    
    # Create the folder if it doesn't exist
    if not os.path.exists(modName):
        os.makedirs(modName)
    
    modLink = mod.get_property("href")
    fileLink = modLink.replace("Module", "File")
    
    links.append({"path": modName, "link": fileLink})
while links:
    fetchItems(links.pop(0))
    
print("Done")
driver.quit()
