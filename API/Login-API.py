import requests
import uuid
import secrets
# Importing uuid, secrets and requests 

email = input("Email: ")
# Email Input
password = input("Password: ")
# Password Input

url = "https://www.guilded.gg/api/login"
# Login API URL

data = {
	"email": email,
	"password": password
	}
# Login API Data

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
# Login API Headers

req = requests.post(url, json=data, headers=headers)
# Login API Request

if "Email not found" in req.text:
	print("Invalid Email, Try Again")
	# Email Invalid 

elif "Email or password is incorrect." in req.text:
	print("Failed Login, Try Again")
	# Failed Login

elif "Must send password to login." in req.text:
	print("Password Is Required, Try Again")
	# Empty Password
	
elif "joinDate" in req.text:
	print("Login Success")
	# Login Success

elif "Must send email to login." in req.text:
	print("Email Is Required, Try Again")
	# Empty Email 

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
