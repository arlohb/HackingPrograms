#!/usr/bin/python3

try:
	import getpass

	pwd = getpass.getpass(prompt="Enter new UNIX password: ")
	pwd2 = getpass.getpass(prompt="Retype new UNIX password: ")
	if pwd == pwd2:
		print("passwd: password updated successfully")
	else:
		print("Sorry, passwords do not match")
		print("passwd: Authentication token manipulation error")
		print("passwd: password unchanged")
except:
	print("\nSorry, passwords do not match")
	print("passwd: Authentication token manipulation error")
	print("passwd: password unchanged")
