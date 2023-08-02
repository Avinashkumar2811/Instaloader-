import instaloader as il

ig=il.Instaloader() #it is a constructor

user=input("Enter the username: ")

ig.download_profile(user,profile_pic_only=True)
