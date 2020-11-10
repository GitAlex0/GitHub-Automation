import os

print("----------------------------------")
print("Started the Github automation")
print("What's next?")
print("1: Just Login")
print("2: Create a new Repo")
print("3: Delete a Repo")
print("----------------------------------")
option = str(input())
if option == "1":
	os.system("github-login.py")
elif option == "2":
	os.system("new-repo.py")
elif option == "3":
	print("Work in Progress!")
	os.system("main.py")
else:
	print("----------------------------------")
	print("This is not an valid option!")
	print("Try Again")
	print("----------------------------------")
	os.system("main.py")