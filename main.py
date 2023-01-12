import os
import sys
import requests
#from dotenv import load_dotenv

#load_dotenv()
#token = os.getenv('TOKEN')
user = "FlorSousa"

len_args = len(sys.argv)
args = sys.argv[1:len_args]

def createIgnore():
    fileHandle = open(".gitignore", "a")
    fileHandle.write(".env\n")
    fileHandle.close()

def download(repository_name) -> int:
    link = "https://www.github.com/{}/{}".format(user,repository_name)
    print(link)
    try:
         response = requests.get(link)
         
    except Exception as e:
        print(e)
        return 1

def download_all() -> int:
    #download all repositories from github api
    return 0

def download_from_file() -> int:
    #download repositories passed in a txt called .repo
    repo = []
    try:
        fileHandle = open(".repo", "r")
        lines = fileHandle.readlines()
        for name in lines:
            name = name.rstrip('\n')
            download(name)
     
        fileHandle.close()
    except:
        return 2
    
    return 0

def reader() -> None:
    status_code = 0
    for index_arg in range(len_args-1):
        if index_arg == 0 and args[index_arg] == '-all':
            status_code = download_all()
            break
        elif args[index_arg] == "-ff":
            status_code = download_from_file()
            break
        else:
            print("Invalid input")
    
    if status_code > 0:
        print("Something got wrong")

createIgnore()
reader()