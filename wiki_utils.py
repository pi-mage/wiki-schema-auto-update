import os
import re
from pdf_to_image import pdf_to_image
from config import *

# reccupération de tous les tableaux que le wiki présente
def get_boards_to_update():
    boards_to_update = []
    files = next(os.walk(WIKI_GIT_FOLDER_ABS), (None, None, []))[2] 
    for file_path in files:
        _, ext = os.path.splitext(file_path)
        if ext.lower() == ".md":
            txt = open(WIKI_GIT_FOLDER_ABS + file_path, 'r').read()
            for board_name in re.findall(r"!\[([A-Za-zÀ-ÖØ-öø-ÿ0-9 ]*)\]\(", txt) : 
                boards_to_update.append(board_name)
    return boards_to_update


# Mise à jour des images et ajout des liens manquants
def update_wiki(boards_to_update, ext_dict):
    files = next(os.walk(WIKI_GIT_FOLDER_ABS), (None, None, []))[2] 
    for file_path in files:
        _, ext = os.path.splitext(file_path)
        if ext.lower() == ".md":
            txt = open(WIKI_GIT_FOLDER_ABS + file_path, 'r').read()
            for board_name in boards_to_update:
                # repo wiki : https://github.com/pi-mage/pi-mage.wiki.git
                # fichier : https://raw.githubusercontent.com/wiki/pi-mage/pi-mage/My_First_Board.jpg
                image_file = board_name + "." + ext_dict[board_name]
                image_path = os.getcwd() + EXPORT_IMG_DIRECTORY + image_file
                image_url = "https://raw.githubusercontent.com/wiki/" + ORGANIZATION_NAME + "/" + REPO_NAME + "/" + image_file.replace(" ", "_") + "?raw=true"
                regex = r'(.*!\[' + board_name + r'\]\(|.*alt="' + board_name + r'" src=")(\).*|".*)'
                txt = re.sub(regex, r'\1' + image_url + r'\2', txt)
                os.system("mv '" + image_path + "' '" + WIKI_GIT_FOLDER_ABS + image_file.replace(" ", "_") + "'")
            open(WIKI_GIT_FOLDER_ABS + file_path, 'w').write(txt)