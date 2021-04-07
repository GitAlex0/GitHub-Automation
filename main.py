import os

print("-"*30)
print("Started the Github automation")
print("What's next?")
print("1: Just Login")
print("2: Create a new Repo")
print("3: Delete a Repo")
print("-"*30)
option = str(input())
if option == "1":
	os.system("github-login.py")
elif option == "2":
	os.system("new-repo.py")
elif option == "3":
	print("Work in Progress!")
	os.system("main.py")
else:
	print("-"*30)
	print("This is not an valid option!")
	print("Try Again")
	print("-"*30)
	os.system("main.py")