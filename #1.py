import requests
link = "https://www.google.com"
f = open("file.txt", "w")
responce = requests.get(link)
f.write(str(responce.text))

