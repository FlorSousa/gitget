import os
import sys
import requests

len_args = len(sys.argv)
args = sys.argv[1:len_args]
def create_folder(cmd):
    path = os.path.dirname(__file__).strip("\\giget")
    try:
         erro_code = os.system("cd "+path+ "&& mkdir repositories && cd repositories &&" + cmd)
         if erro_code == 1 or erro_code == 256: os.system("cd "+path+ " && cd repositories &&" + cmd)
    except:
         os.system("cd "+path+ " && cd repositories &&" + cmd)

def download(repository_name) -> int:
    user = args[0].strip("--from=")
    link = "https://www.github.com/{}/{}".format(user,repository_name)
    print("Repositorio: "+link)
    try:
         cmd = "git clone " + link
         create_folder(cmd)
         
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
        
reader()