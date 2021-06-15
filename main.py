from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from datetime import datetime
from pdf_to_image import pdf_to_image
from scenarios import first_retrieval, retrieval
import os
from config import *
from wiki_utils import get_boards_to_update, update_wiki


# définition du driver navigateur + dossier de telechargement
options = webdriver.ChromeOptions()
# https://stackoverflow.com/a/63727460
preferences = {
    "download.default_directory": os.getcwd() + EXPORT_PDF_DIRECTORY , # pass the variable
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True 
}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)

ext_dict = dict()




for it, (board_name, url) in enumerate(WEBPAGES.items()):
    if(it == 0):    first_retrieval(driver, url, EMAIL, PASSWORD)
    else :          retrieval(driver, url)
    ext_dict[board_name] = pdf_to_image("." + EXPORT_PDF_DIRECTORY + board_name + ".pdf", "." + EXPORT_IMG_DIRECTORY + board_name)

os.system(CD_GIT + "git pull")

boards_to_update = get_boards_to_update()
update_wiki(boards_to_update, ext_dict)

os.system(CD_GIT + "git add *")
os.system(CD_GIT + "git commit -m 'miro-images-update-" + datetime.now().strftime("%dd-%mm-%Yy-%Hh-%Mm-%Ss") + "'")
os.system(CD_GIT + "git push https://" + GIT_LOGIN + ":" + GIT_PASSWORD + "@github.com/" + ORGANIZATION_NAME + "/" + REPO_NAME + ".wiki.git")

