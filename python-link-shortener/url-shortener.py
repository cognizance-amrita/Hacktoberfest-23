# url Shortener
import requests

api = "https://ulvis.net/api.php"   
long_url = input("Enter url to shorten : ")
custom = input("Enter custom name (optional): ")
arguments = {"url":long_url, "custom":custom}
short = requests.get(api, arguments)
print(short.text)
