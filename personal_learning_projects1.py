boss="Tyler"
assistant="jalen"
boss_code="24"
ass_code="08"
boss_secondcode="2407"
ass_codez="2408"
admin_login=input("Enter Passcode")

if admin_login==boss_code:
    print("welcome Tyler")
    second_pass=input("enter second passcode")
    if second_pass==boss_secondcode:
        print("thank you sir")

        report=input("enter report Number")
        if report=="1":
            print("finiacial report")
        elif report=="2":
            print("cash money")
    else:
     print("wrong! try again!")

elif admin_login==ass_code:
    print("welcome jalen")
    ass_code2=input("enter second code")
    if ass_code2==ass_codez:
        print("thank you assistant")
else:
    print("wrong password")
