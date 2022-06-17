import pyshorteners

def short_the_url():
    link = input("\nenter link here :")
    small = pyshorteners.Shortener()
    x = small.tinyurl.short(link)
    print("Your url :",x,"\n")

b = short_the_url()

ans = True

while ans == True:
    a=input("Want to short more Link's ? \n(yes,no):")
    no_list=["N","NO","n","no"]
    yes_list=["Y","YES","y","yes"]
    if a in no_list:
        break
    if a in yes_list:
        short_the_url()
    else:
        continue
    
    
