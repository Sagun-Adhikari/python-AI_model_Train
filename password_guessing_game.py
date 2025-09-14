import random
password= input("inter your password: ")
if len(password)<6 and len(password)<2:
    print("password too short or long")
    exit()
strlen=len(password)
h1=password[0]
h2=password[strlen-1]
h3=password[2]
print(f"your hint are first letter iS {h1}, last letter is {h2}, 3rd letter is {h3}")
for i in range(3):
    guess=input("guess your password: ")
    if guess==password:
        print("correct") 
        exit()
    else:
        print("wrong")  

