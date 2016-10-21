import requests
newname = requests.get("https://www.nikhil.info.np")
print(newname)
if newname.status_code == 200:
	print (newname.text)
else:
	print("there was an error loading this page")