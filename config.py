import os

REPO_NAME = "garbage"
ORGANIZATION_NAME = "pi-mage"
EXPORT_PDF_DIRECTORY = "/exports_pdf/"
EXPORT_IMG_DIRECTORY = "/exports_image/"
WIKI_GIT_FOLDER = "/git_wiki/"
WIKI_GIT_FOLDER_ABS = os.getcwd() + WIKI_GIT_FOLDER
CD_GIT = "cd ." + WIKI_GIT_FOLDER + ";"
WEBPAGES = {
    "My First Board" : "https://miro.com/welcomeonboard/C9QPkEPlHyHQyAdC9LLnZ9y00x3p09rrxzDsoybz8qYTzSAzoIq5FqHYW8Qs6pfn"
}
LAST_COMMIT = 'git log | grep commit | egrep -io "[a-z0-9]{40}" | head -1'

EMAIL = os.environ['MIRO_EMAIL']
PASSWORD = os.environ['MIRO_PASSWORD']

GIT_LOGIN = os.environ['GIT_LOGIN']
GIT_PASSWORD = os.environ['GIT_PASSWORD']
