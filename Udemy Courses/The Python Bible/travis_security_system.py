
known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi! my name is Travis")
    name = input("What is your name?: ").strip().lower().capitalize() #good to use strip to deal with accidental extra spaces

    if name in known_users:
        print("name recognized")
    else: 
        print("name not recognized")
