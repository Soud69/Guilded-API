import requests
import uuid
import secrets
# Importing uuid, secrets and requests 

username = input("Username: ")
# Username Input
email = input("Email: ")
# Email Input
password = input("Password: ")
# Password Input

url = "https://www.guilded.gg/api/users?type=email"
# Reg API URL

data = {
	"email": email,
	"password": password,
	"extraInfo": {
		
	},
	"name": username,
	"fullName": username
	}
# Reg API Data

headers = {
	"Host": "www.guilded.gg",
	"Accept": "application/json",
	"guilded-nonprod-waf-pw": "null",
	"guilded-device-id": str(uuid.uuid4()).upper(),
	"Accept-Language": "en-us",
	"Accept-Encoding": "gzip, deflate, br",
	"Content-Type": "application/json",
	"guilded-client-id": str(uuid.uuid4()),
	"User-Agent": "Guilded/7.1.7 CFNetwork/1206 Darwin/20.1.0",
	"guilded-stag": str(secrets.token_hex(8*2)),
	"Connection": "keep-alive"
	} 
# Reg API Headers

req = requests.post(url, json=data, headers=headers)
# Reg API Request

if "Email is invalid." in req.text:
	print("Invalid Email, Try Again")
	# Email Invalid 

elif "User with this email already exists." in req.text:
	print("Email Is Used, Try Again")
	# Used Email

elif "Password is required" in req.text:
	print("Password Is Required, Try Again")
	# Empty Password
	
elif f'name":"{username}' in req.text:
	print("Reg Success")
	# Reg Success

elif "Email is required" in req.text:
	print("Email Is Required, Try Again")
	# Empty Email 

elif "Name is required" in req.text:
	print("Name Is Required, Try Again")	
	# Empty Username

elif "Name contains invalid characters." in req.text:
	print("Username Have Invalid Characters, Try Again")
	# Used Email

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
