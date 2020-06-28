from canvasapi import Canvas
import os
import threading
import requests

def down(link, filelocation):
    r = requests.get(link, stream=True)
    with open(filelocation, 'wb') as f:
    	f.write(r.content)

def main():
	API_KEY = input("Enter your API key (Make sure there are no spaces): ")
	API_URL = input("Enter your schools canvas link (e.g. school.instructure.com/): ")
	userid = input("Enter your user id (Go to your profile and then select on of the options, and then click on your name. Your user id will be the 3-5 numbers at the end of the url): ")
	operatingsystem = input("Are running Windows (Type 1) or Mac Os (Type 2): ")
	canvas = Canvas(API_URL, API_KEY)
	user = canvas.get_user(userid)
	folders = user.get_folders()
	if(operatingsystem == "1"):
		for folder in folders:
			folpath = str(folder).replace("/", "\\")
			folpath = folpath.replace(" ", "-")
			folpath = folpath.replace(":", "-")
			path1 = "Canvas_Files\\"+folpath
			if not os.path.exists(path1):
				os.makedirs(path1)
			files = folder.get_files()
			for file in files:
				loc = path1+"\\"+str(file)
				url = file.download()
				print("Downloading ", str(file), end="\r")
				down(url, loc)
				print("                                                                               ", end="\r")
		print("Finished")
	if(operatingsystems=="2"):
		for folder in folders:
			folpath = str(folder).replace(" ", "-")
			folpath = folpath.replace(":", "-") #Not sure if macs have issues with ":" in folder names
			path1 = "Canvas_Files/"+folpath
			if not os.path.exists(path1):
				os.makedirs(path1)
			files = folder.get_file()
			for file in files:
				loc = path1+"/"+str(file)
				url = file.download()
				print("Downloading ", str(file), end="\r")
				down(url, loc)
				print("                                                                               ", end="\r")
		print("Finished")
	else:
		print("Your input is not 1 or 2")



main()